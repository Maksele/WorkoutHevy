class Muscle:
    # Represents a muscle group and tracks training data.
    def __init__(self, name):
        self.name = name
        self.worked_sets = 0 #maybe not needed
        self.worked_reps = 0
        self.worked_volume = 0
        self.history = []  # stores session data over time

    def train(self, reps, weight, date):
        sets = len(reps)
        total_reps = sum(reps)
        total_volume = [r * w for r, w in zip(reps, weight)]

        # Update running totals
        self.worked_sets += sets
        self.worked_reps += total_reps
        self.worked_volume += sum(total_volume)

        # Log this workout for data analysis
        self.history.append({
            "date": date,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "volume": total_volume
        })

    #Helps print muscle summary
    def __str__(self):
        return (
            f"{self.name.capitalize()}: "
            f"{self.worked_sets} sets, "
            f"{self.worked_reps} reps, "
            f"{self.worked_volume} kg total"
        )


# ----------------- Create all muscles based on muscle group (Maybe later even split them into muscle heads?) -----------------
chest = Muscle("chest")
triceps = Muscle("triceps")
shoulders = Muscle("shoulders")

biceps = Muscle("biceps")
upper_back = Muscle("upper back")
lower_back = Muscle("lower back")

forearms = Muscle("forearms")
traps = Muscle("traps")
abs = Muscle("abs")
obliques = Muscle("obliques")

quads = Muscle("quads")
glutes = Muscle("glutes")
hamstrings = Muscle("hamstrings")
calves = Muscle("calves")
adductor = Muscle("adductor")
abductor = Muscle("abductor")


def get_all_muscles():
    return [
        calves,
        hamstrings,
        adductor,
        abductor,
        quads,
        glutes,
        lower_back,
        upper_back,
        traps,
        obliques,
        abs,
        chest,
        shoulders,
        biceps,
        triceps,
        forearms,
    ]




# ----------------- Exercise Classes -----------------

class Exercise:
    """Base class for all exercises (provides consistent __repr__)"""

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def train(self, date, reps, weight):
        for m in self.muscles:
            m.train(reps, weight, date)
        sets = len(reps)
        total_volume = [r * w for r, w in zip(reps, weight)]
        self.history.append({
            "date": date, "reps": reps, "weight": weight, "sets": sets, "volume": total_volume,
            "equipment": self.equipment, "grip": self.grip, "execution": self.execution
        })
    

class BackExtension(Exercise):
    usual_equipment = ["dumbell", "bodyweight", "barbell", "machine"]

    def __init__(self, equipment="dumbell", grip="neutral", execution="simultaneous"):
        self.name = "back extension"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [lower_back, glutes, hamstrings]
        self.history = []


class BenchPress(Exercise):
    usual_equipment = ["barbell", "dumbbell", "machine", "smith"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "bench press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, triceps, shoulders]
        self.history = []


class BicepCurl(Exercise):
    usual_equipment = ["dumbbell", "barbell", "cable"]

    def __init__(self, equipment="dumbbell", grip="underhand", execution="simultaneous"):
        self.name = "bicep curl"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [biceps]
        self.history = []


class CalfRaise(Exercise):
    usual_equipment = ["smith", "machine", "barbell", "dumbbell"]

    def __init__(self, equipment="machine", grip="standard", execution="simultaneous"):
        self.name = "calf raise"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [calves]
        self.history = []


class ChestFly(Exercise):
    usual_equipment = [ "machine", "dumbbell", "cable"]

    def __init__(self, equipment="dumbbell", grip="overhand", execution="simultaneous"):
        self.name = "chest fly"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, shoulders]
        self.history = []


class Deadlift(Exercise):
    usual_equipment = ["barbell", "dumbbell", "smith"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "deadlift"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [lower_back, glutes, hamstrings, quads]
        self.history = []


class HipThrust(Exercise):
    usual_equipment = ["barbell", "machine", "dumbell", "bodyweight"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "hip thrust"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [glutes, hamstrings]
        self.history = []


class InclineBenchPress(Exercise):
    usual_equipment = ["dumbbell", "barbell", "smith", "machine"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "incline bench press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, triceps, shoulders]
        self.history = []


class LateralRaise(Exercise):
    usual_equipment = ["cable", "dumbbell", "machine"]

    def __init__(self, equipment="cable", grip="overhand", execution="simultaneous"):
        self.name = "lateral raise"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [shoulders]
        self.history = []


class LegPress(Exercise):
    usual_equipment = ["machine"]

    def __init__(self, equipment="machine", grip="standard", execution="simultaneous"):
        self.name = "leg press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
        self.history = []


class Lunge(Exercise):
    usual_equipment = ["dumbbell", "bodyweight", "barbell"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="sequential"):
        self.name = "lunge"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
        self.history = []


class OverheadPress(Exercise):
    usual_equipment = ["machine", "dumbbell", "barbell" , "smith"]

    def __init__(self, equipment="dumbbell", grip="overhand", execution="simultaneous"):
        self.name = "overhead press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [shoulders, triceps]
        self.history = []


class PreacherCurl(Exercise):
    usual_equipment = ["barbell", "dumbbell"]

    def __init__(self, equipment="barbell", grip="underhand", execution="simultaneous"):
        self.name = "preacher curl"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [biceps, forearms]
        self.history = []


class Pulldown(Exercise):
    usual_equipment = ["cable", "machine"]

    def __init__(self, equipment="cable", grip="overhand wide", execution="simultaneous"):
        self.name = "pulldown"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps]
        self.history = []


class PullUp(Exercise):
    usual_equipment = ["bodyweight", "assisted", "weighted"]

    def __init__(self, equipment="bodyweight", grip="overhand", execution="simultaneous"):
        self.name = "pullup"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps]
        self.history = []


class ReverseFly(Exercise):
    usual_equipment = ["machine", "cable", "dumbbell"]

    def __init__(self, equipment="cable", grip="overhand", execution="simultaneous"):
        self.name = "reverse fly"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, shoulders]
        self.history = []


class RomanianDeadlift(Exercise):
    usual_equipment = ["barbell", "dumbbell", "smith"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "romanian deadlift"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [hamstrings, glutes, lower_back]
        self.history = []


class SeatedRow(Exercise):
    usual_equipment = ["cable", "machine", "dumbbell"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="sequential"):
        self.name = "seated row"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps, traps]
        self.history = []


class ShoulderPress(Exercise):
    usual_equipment = ["machine", "dumbbell", "barbell", "smith"]

    def __init__(self, equipment="dumbell", grip="overhand", execution="simultaneous"):
        self.name = "shoulder press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [shoulders, triceps]
        self.history = []


class Shrugs(Exercise):
    usual_equipment = ["dumbbell", "barbell"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="simultaneous"):
        self.name = "shrugs"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [traps]
        self.history = []


class Squat(Exercise):
    usual_equipment = ["barbell", "dumbbell", "smith", "bodyweight"]

    def __init__(self, equipment="barbell", grip="overhand", execution="simultaneous"):
        self.name = "squat"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
        self.history = []


class StandingRow(Exercise):
    usual_equipment = ["Barbell", "Dumbbell", "smith"]
    def __init__(self, equipment="Barbell", grip="overhand", execution="simultaneous"):
        self.name = "standing row"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps, traps]
        self.history = []


class TricepPushdown(Exercise):
    usual_equipment = ["cable", "band"]

    def __init__(self, equipment="cable", grip="neutral", execution="simultaneous"):
        self.name = "tricep pushdown"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [triceps]
        self.history = []

    def train(self, date, reps, weight):
        for m in self.muscles:
            m.train(reps, weight, date)
        sets = len(reps)
        total_volume = [r * w for r, w in zip(reps, weight)]
        self.history.append({
            "date": date, "reps": reps, "weight": weight, "sets": sets, "volume": total_volume,
            "equipment": self.equipment, "grip": self.grip, "execution": self.execution
        })


def get_all_exercises():
    return [
        BackExtension(),
        BenchPress(),
        BicepCurl(),
        CalfRaise(),
        ChestFly(),
        Deadlift(),
        HipThrust(),
        InclineBenchPress(),
        LateralRaise(),
        LegPress(),
        Lunge(),
        OverheadPress(),
        PreacherCurl(),
        Pulldown(),
        PullUp(),
        ReverseFly(),
        RomanianDeadlift(),
        SeatedRow(),
        ShoulderPress(),
        Shrugs(),
        Squat(),
        StandingRow(),
        TricepPushdown()
    ]