from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from istory_bot import IStoryBot
import os
from query_groq import query_groq


class ElderStoryBot(IStoryBot):
    def __init__(self, messages, user_image=None):
        self.messages = messages
        self.user_image = user_image

    def generate_story(self):
        story_prompt = {
            "role": "system",
            "content": """Create a blog post from the following conversation. 
            The blog post should:
            1. Have an engaging title
            2. Be structured in clear sections
            3. Focus on the most interesting life stories and insights shared
            4. Include direct quotes when relevant
            5. Have a thoughtful conclusion
            6. Be between 500-1000 words
            7. Don't use markdown, because the final format will be a pdf.
            Format the response with the title on top, followed by the content in paragraphs.""",
        }

        # Create a temporary message list for story generation
        story_messages = [
            story_prompt,
            {"role": "user", "content": str(list(self.messages))},
        ]

        blog_post = query_groq(story_messages, model="llama-3.1-70b-versatile")
        self.save_as_pdf(blog_post)
        return blog_post

    def save_as_pdf(self, blog_content):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"elder_story_{timestamp}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "CustomTitle", parent=styles["Heading1"], fontSize=24, spaceAfter=30
        )

        content_parts = blog_content.split("\n", 1)
        title = content_parts[0]
        body = content_parts[1] if len(content_parts) > 1 else ""

        story = []
        story.append(Paragraph(title, title_style))

        if self.user_image and os.path.exists(self.user_image):
            img = Image(self.user_image, width=300, height=300)
            story.append(img)
        story.append(Spacer(1, 20))

        for paragraph in body.split("\n\n"):
            if paragraph.strip():
                story.append(Paragraph(paragraph, styles["Normal"]))
                story.append(Spacer(1, 12))

        doc.build(story)
        return filename
