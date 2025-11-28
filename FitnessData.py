import json
import exercises
import os
import matplotlib.pyplot as plt
import code
from datetime import datetime, timedelta



past_workouts_folder = "past_workouts"  # folder containing all {date}.txt files
all_muscles = exercises.get_all_muscles() # List of all Muscle objects
all_muscles_dict = {muscle.name: muscle for muscle in all_muscles} # Dictionary of all muscles by name

all_exercises_data = [] # List to store all exercised performed in past sessions
all_exercises = exercises.get_all_exercises() # List of all Exercise objects
all_exercises_dict = {exercise.name: exercise for exercise in all_exercises} # Dictionary of all exercises by name

def filter_exercises(exercise_list, equipment=None, grip=None, execution=None): 
    """
    Filters the given exercise_list based on the provided criteria and returns a new one
    """
    filtered_exercise_list = exercise_list

    if equipment:
        filtered_exercise_list = [ex for ex in filtered_exercise_list if equipment in ex.usual_equipment]
    if grip:
        filtered_exercise_list = [ex for ex in filtered_exercise_list if ex.grip == grip]
    if execution:
        filtered_exercise_list = [ex for ex in filtered_exercise_list if ex.execution == execution]

    return filtered_exercise_list

def plot_progression(muscle_or_exercise, metric="weight"):
    """
    Plots progression of a given metric (weight, reps, sets or volume) over time for a muscle or exercise.
    """
    dates = []
    values = []
    date_previous = None
    for record in sorted(muscle_or_exercise.history, key=lambda x: x["date"]):
        fmt = "%Y-%m-%d"  # Format to parse the date
        date = record["date"]
        date = datetime.strptime(date, fmt)
        
        if metric == "weight":
            value = max(record["weight"])
        elif metric == "reps":
            value = sum(record["reps"])
        elif metric == "volume":
            value = sum(record["volume"])
        elif metric == "sets":
            value = record["sets"]
        else:
            raise ValueError(f"Unknown metric '{metric}'")
        if date == date_previous:
            # Update the last entry
            values[-1] += value
        else:           
            dates.append(date)
            values.append(value)
        
        date_previous = date
    
    # Check if there is data to plot
    if not values:
        print(f"No data to plot for {muscle_or_exercise.name} ({metric})")
        return
    
    # --- Plot styling ---
    
    fig, ax = plt.subplots(facecolor="#0d0d0d")
    ax.set_facecolor("#0d0d0d")
    ax.set_ylim(0, max(x for x in values if x is not None) * 1.1)
    ax.plot(dates, values, marker='o', color="#00bfff", linewidth=2)
    ax.set_title(f"{muscle_or_exercise.name.capitalize()} Progression ({metric.capitalize()})", color="white")
    ax.set_xlabel("Date", color="white")
    ax.set_ylabel(metric.capitalize(), color="white")

    ax.tick_params(colors="white")
    ax.grid(color=(0.749, 0.749, 0.749), linestyle="--", alpha=0.3)

    plt.style.use('dark_background')

    #Use date objects to create accurate intervals between ticks
    plt.xticks(dates, [d.strftime(fmt) for d in dates], rotation=90) 
    plt.tight_layout()
    plt.show()

# Loop through all wokrout files and train muscles/exercises accordingly, 
# storing data in all_exercises_data and each muscle / exercise history
for filename in sorted(os.listdir(past_workouts_folder)):
    if filename.endswith(".txt"):
        filepath = os.path.join(past_workouts_folder, filename)
        with open(filepath, "r") as f:
            session_data = json.load(f)

        date = session_data["date"]

        for ex_data in session_data["exercises"]:
            # find the exercise object by name
            exercise_obj = None
            for ex in all_exercises:
                if ex.name == ex_data["exercise_name"]:
                    exercise_obj = ex
                    break

            #check if exercise was found among all_exercises
            if not exercise_obj:
                print(f"Unknown exercise: {ex_data['exercise_name']}")
                continue
            
            if "grip" in ex_data:
                exercise_obj.grip = ex_data["grip"]
            if "execution" in ex_data:
                exercise_obj.execution = ex_data["execution"]
            if "equipment" in ex_data:
                exercise_obj.equipment = ex_data["equipment"]

            #train the muscles assciated with the exercise
            exercise_obj.train(date, ex_data["reps"], ex_data["weight"])
            #add the exercise data to all_exercises_data, for future data analysis
            all_exercises_data.append(exercise_obj)

def add_workout_session():
    """
    Adds a new workout session to the past_workouts folder.
    exercises_performed: list of dicts with keys: exercise_name, reps (list), weight (list), grip (optional), execution (optional), equipment (optional)
    """
    parameter_not_valid = True
    while parameter_not_valid:
        parameter_not_valid = False
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if date == "":
            date = datetime.now()
        else:
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                parameter_not_valid = True
    
    parameter_not_valid = True
    while parameter_not_valid:  
        parameter_not_valid = False
        num_exercises = input("Enter number of exercises performed: ")
        try:
            num_exercises = int(num_exercises)
            if num_exercises <= 0:
                print("Number of exercises must be positive.")
                parameter_not_valid = True
        except ValueError:
            print("Invalid number. Please enter a positive integer.")
            parameter_not_valid = True

    parameter_not_valid = True

    exercises_performed = []

    for i in range(num_exercises):
        print(f"Exercise {i+1}:")
        
        while parameter_not_valid:  
            parameter_not_valid = False
            exercise_name = input("  Enter exercise name: ").lower()
            if exercise_name not in all_exercises_dict:
                print("  Unknown exercise. Please enter a valid exercise name.")
                parameter_not_valid = True
        parameter_not_valid = True

        exercise_obj = all_exercises_dict[exercise_name]

        while parameter_not_valid:
            parameter_not_valid = False
            reps_input = input("  Enter reps (comma-separated): ")
            weight_input = input("  Enter weight (comma-separated): ")
        
            try:
                reps = [int(r.strip()) for r in reps_input.split(",")]
                weight = [float(w.strip()) for w in weight_input.split(",")]
                if len(reps) != len(weight):
                    print("  Number of reps and weights must match.")
                    parameter_not_valid = True
            except ValueError:
                parameter_not_valid = True
                print("  Invalid input for reps or weight. Please enter numbers only.")
        parameter_not_valid = True

        grip = input("  Enter grip [neutral / reverse...] (optional, press Enter to skip): ")
        execution = input("  Enter execution [simultaneous / sequential or custom] (optional, press Enter to skip): ")
        equipment = input("  Enter equipment [dumbell / barbell / cable / machine / freeweight...] (optional, press Enter to skip): ")
        
        exercise_data = {
            "exercise_name": exercise_name,
            "reps": reps,
            "weight": weight
        }
        if grip:
            exercise_data["grip"] = grip
        if execution:
            exercise_data["execution"] = execution
        if equipment:
            exercise_data["equipment"] = equipment
        
        exercises_performed.append(exercise_data)
    
    
    

    
    session_data = {
        "date": date,
        "exercises": exercises_performed
    }
    print(session_data)

    filename = f"{date.strftime('%Y-%m-%d')}.txt"
    filepath = os.path.join(past_workouts_folder, filename)
    with open(filepath, "w") as f:
        json.dump(session_data, f, indent=4)


def help(command=None):
    if command is None:
        print("Available commands:")
        print(" - filter_exercises()")
        print(" - plot_progression()")
        print(" - all_muscles_dict: dictionary of all muscles by name")
        print(" - all_exercises_dict: dictionary of all exercises by name")
        print("Type help('command_name') for more details.")

    elif command == "filter_exercises":
        print("filter_exercises(exercise_list, equipment=None, grip=None, execution=None)")
        print("Filters the given exercise_list based on the provided criteria.")
        print("Parameters:")
        print(" - exercise_list: list of Exercise objects to filter (like all_exercises)")
        print(" - equipment: filter by equipment type ('barbell', 'dumbbell', 'freeweight','machine'....) (string)")
        print(" - grip: filter by grip type (neutral, reverse...)(string)")
        print(" - execution: filter by execution type (simultanious, sequential) (string)")
        print("Returns a list of Exercise objects that match the criteria.")

    elif command == "plot_progression":
        print("plot_progression(muscle_or_exercise, metric='weight')")
        print("Plots progression of a given metric over time for a muscle or exercise.")
        print("Parameters:")
        print(" - muscle_or_exercise: Muscle or Exercise object to plot progression for")
        print(" - metric: metric to plot ('weight', 'reps', 'sets', 'volume') (string)")
        print("Displays a plot of the specified metric over time.")

    elif command == "all_muscles_dict":
        print("all_muscles_dict: dictionary of all muscles by name")
        print(all_muscles_dict)

    elif command == "all_exercises_dict":
        print("all_exercises_dict: dictionary of all exercises by name")
        print(all_exercises_dict)

    else:
        print(f"No help available for '{command}'")

if __name__ == "__main__":
    print("Type 'help()' for available commands")

    # Launch an interactive console
    code.interact(local=globals())
