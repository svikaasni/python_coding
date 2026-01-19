def daily_task_manager():
    print("--- 🌅 Morning: Create Your Checklist ---")
    print("Enter your tasks one by one. Type 'done' when you are finished.")
    
    checklist = []
    while True:
        task = input("Add task: ").strip()
        if task.lower() == 'done':
            break
        if task:
            checklist.append(task)
    
    if not checklist:
        print("No tasks added. Have a great day!")
        return

    print(f"\n✅ Checklist created with {len(checklist)} tasks.")
    print("-" * 40)
    
    # Simulate the end of the day
    input("\nPress Enter when you are ready to review your day... 🌙")
    
    completed_tasks = []
    incomplete_tasks = []
    
    print("\n--- 📝 Evening Review ---")
    for task in checklist:
        while True:
            status = input(f"Did you finish '{task}'? (y/n): ").lower().strip()
            if status == 'y':
                completed_tasks.append(task)
                break
            elif status == 'n':
                incomplete_tasks.append(task)
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    # Final Summary
    print("\n" + "="*30)
    print("       DAILY SUMMARY")
    print("="*30)
    
    print(f"\n🎉 COMPLETED TASKS ({len(completed_tasks)}):")
    if completed_tasks:
        for item in completed_tasks:
            print(f"  [✓] {item}")
    else:
        print("  None yet. Keep pushing!")

    print(f"\n⏳ INCOMPLETE TASKS ({len(incomplete_tasks)}):")
    if incomplete_tasks:
        for item in incomplete_tasks:
            print(f"  [ ] {item}")
    else:
        print("  Amazing! Everything is done.")
    
    print("\n" + "="*30)

if __name__ == "__main__":
    daily_task_manager()