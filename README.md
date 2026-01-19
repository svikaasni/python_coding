📅 Daily Task OrganizerA lightweight Python utility designed to help users bridge the gap between morning intentions and evening reflections. This tool categorizes tasks into Completed and Incomplete lists to provide a clear overview of daily productivity.🚀 How It WorksThe program follows a simple three-step workflow:Plan: Create a checklist of tasks at the start of the day.Review: At the end of the day, mark each task as finished ($y$) or unfinished ($n$).Analyze: View a categorized summary of your progress to help plan for the next day.🛠️ FeaturesDynamic Checklist Creation: Add as many tasks as you need.Interactive Review: Step-by-step confirmation for each task.Formatted Summary: Clean visual output of what was accomplished and what still needs attention.Input Validation: Ensures only valid responses are accepted during the review process.💻 Installation & UsagePrerequisitesPython 3.x installed on your machine.Running the ProgramClone this repository or download the script:Bashgit clone https://github.com/your-username/daily-task-organizer.git
Navigate to the project folder:Bashcd daily-task-organizer
Run the script:Bashpython task_manager.py
📋 Example OutputPlaintext--- 📝 Evening Review ---
Did you finish 'Exercise'? (y/n): y
Did you finish 'Read 20 pages'? (y/n): n

🎉 COMPLETED TASKS (1):
  [✓] Exercise

⏳ INCOMPLETE TASKS (1):
  [ ] Read 20 pages
🛣️ Roadmap[ ] Add persistent storage (save tasks to a .txt or .json file).[ ] Add timestamps to track when tasks were completed.[ ] Create a GUI (Graphical User Interface) version.
