import os
import slack_sdk
from notion_client import Client
from openai import OpenAI

class MeetingSummarizer:
    def __init__(self):
        # Initialize clients with environment variables
        self.slack_client = slack_sdk.WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
        self.notion_client = Client(auth=os.environ.get('NOTION_API_KEY'))
        self.openai_client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    def transcribe_slack_meeting(self, channel_id, thread_ts):
        """
        Retrieve meeting transcript from Slack thread
        """
        try:
            # Fetch thread messages
            thread_messages = self.slack_client.conversations_replies(
                channel=channel_id,
                ts=thread_ts
            )
            
            # Combine messages into transcript
            transcript = "\n".join([
                f"{msg['user']}: {msg['text']}" 
                for msg in thread_messages['messages']
            ])
            
            return transcript
        except Exception as e:
            print(f"Error retrieving Slack transcript: {e}")
            return None

    def generate_ai_summary(self, transcript):
        """
        Use AI to generate a concise meeting summary
        """
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert meeting summarizer."},
                    {"role": "user", "content": f"Provide a concise summary of this meeting transcript:\n\n{transcript}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating AI summary: {e}")
            return None

    def save_to_notion(self, summary, page_id):
        """
        Save meeting summary to Notion page
        """
        try:
            self.notion_client.pages.update(
                page_id=page_id,
                properties={
                    "Summary": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": summary}
                            }
                        ]
                    }
                }
            )
            print("Summary successfully saved to Notion")
        except Exception as e:
            print(f"Error saving to Notion: {e}")

    def process_meeting(self, slack_channel, thread_ts, notion_page_id):
        """
        Orchestrate entire meeting summarization workflow
        """
        # Step 1: Retrieve Slack thread transcript
        transcript = self.transcribe_slack_meeting(slack_channel, thread_ts)
        if not transcript:
            return False

        # Step 2: Generate AI summary
        summary = self.generate_ai_summary(transcript)
        if not summary:
            return False

        # Step 3: Save to Notion
        self.save_to_notion(summary, notion_page_id)
        
        return True

def main():
    summarizer = MeetingSummarizer()
    
    # Example usage (would typically be triggered by an event or scheduled)
    summarizer.process_meeting(
        slack_channel='C01MEETING123', 
        thread_ts='1234567890.000000',
        notion_page_id='abc123def456'
    )

if __name__ == "__main__":
    main()