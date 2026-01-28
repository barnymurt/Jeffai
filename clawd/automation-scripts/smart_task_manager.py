import os
from trello import TrelloClient
from slack_sdk import WebClient
from anthropic import Anthropic

class SmartTaskManager:
    def __init__(self):
        # Initialize clients with environment variables
        self.trello_client = TrelloClient(
            api_key=os.environ.get('TRELLO_API_KEY'),
            token=os.environ.get('TRELLO_TOKEN')
        )
        self.slack_client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
        self.anthropic_client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

    def analyze_task_complexity(self, task_description):
        """
        Use AI to analyze task complexity and suggest optimal approach
        """
        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=300,
                messages=[
                    {
                        "role": "user",
                        "content": f"Analyze the complexity of this task and provide insights:\n{task_description}\n\n"
                        "Break down the task and suggest:\n"
                        "1. Estimated effort (low/medium/high)\n"
                        "2. Key subtasks\n"
                        "3. Potential challenges\n"
                        "4. Recommended workflow approach"
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            print(f"AI analysis error: {e}")
            return None

    def create_trello_card(self, board_name, list_name, task_details):
        """
        Create a Trello card with AI-enhanced details
        """
        try:
            # Find the specific board and list
            board = next((b for b in self.trello_client.list_boards() if b.name == board_name), None)
            if not board:
                raise ValueError(f"Board '{board_name}' not found")

            task_list = next((l for l in board.list_lists() if l.name == list_name), None)
            if not task_list:
                raise ValueError(f"List '{list_name}' not found in board")

            # Create card with AI-enhanced description
            card = task_list.add_card(
                name=task_details['title'],
                desc=task_details['ai_analysis']
            )
            return card.short_url
        except Exception as e:
            print(f"Trello card creation error: {e}")
            return None

    def notify_slack(self, channel, task_details):
        """
        Send task notification to Slack
        """
        try:
            self.slack_client.chat_postMessage(
                channel=channel,
                text=f"🚀 New Smart Task Created:\n"
                     f"*{task_details['title']}*\n"
                     f"Trello Link: {task_details['trello_link']}\n\n"
                     f"*AI Insights:*\n{task_details['ai_analysis']}"
            )
        except Exception as e:
            print(f"Slack notification error: {e}")

    def process_new_task(self, task_description, board_name, list_name, slack_channel):
        """
        Full workflow for processing a new task
        """
        # Step 1: AI-powered task complexity analysis
        ai_analysis = self.analyze_task_complexity(task_description)
        if not ai_analysis:
            print("Task analysis failed")
            return False

        # Step 2: Create Trello card
        trello_link = self.create_trello_card(board_name, list_name, {
            'title': task_description.split('\n')[0],
            'ai_analysis': ai_analysis
        })
        if not trello_link:
            print("Trello card creation failed")
            return False

        # Step 3: Notify via Slack
        self.notify_slack(slack_channel, {
            'title': task_description.split('\n')[0],
            'trello_link': trello_link,
            'ai_analysis': ai_analysis
        })

        return True

def main():
    task_manager = SmartTaskManager()
    
    # Example usage
    task_manager.process_new_task(
        task_description="Develop a comprehensive marketing strategy for Q3",
        board_name="Marketing Projects",
        list_name="Backlog",
        slack_channel="#marketing-team"
    )

if __name__ == "__main__":
    main()