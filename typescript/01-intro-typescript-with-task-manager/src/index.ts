enum Priority {
    Low = "LOW",
    Medium = "MEDIUM",
    High = "HIGH",
}

interface Task {
    id: number;
    title: string;
    description: string;
    isCompleted: boolean;
    priority: Priority;
    dueDate?: Date;
}


class TaskManager {
    private tasks: Task[] = [];

    public addTask(task: Task): void {
        this.tasks.push(task);
        console.log(`✨Task added: "${task.title}"`);
    }

    public getAllTasks(): Task[] {
        return this.tasks;
    }

    public markCompleted(taskId: number): void {
        for (const task of this.tasks) {
            if (task.id === taskId) {
                task.isCompleted = true;
                break;
            }
        }
    }
}



const task1: Task = {
    id: 1,
    title: "Do the laundry",
    description: "You have to do the laundry.",
    isCompleted: false,
    priority: Priority.Medium,
    dueDate: new Date(),
}

const myManager = new TaskManager();
myManager.addTask(task1);

console.log("Current Tasks:", myManager.getAllTasks());