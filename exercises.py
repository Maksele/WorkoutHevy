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
        return f"{self.__class__.__name__}(equipment='{self.equipment}', grip='{self.grip}', execution='{self.execution}')"


class BenchPress(Exercise):
    usual_equipment = ["barbell", "dumbbell", "machine"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Bench Press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, triceps, shoulders]
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


class InclineBenchPress(Exercise):
    usual_equipment = ["barbell", "dumbbell", "machine"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Incline Bench Press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, triceps, shoulders]
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


class ChestFly(Exercise):
    usual_equipment = ["dumbbell", "machine", "cable"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="simultaneous"):
        self.name = "Chest Fly"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [chest, shoulders]
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


class PullUp(Exercise):
    usual_equipment = ["bodyweight", "assisted machine"]

    def __init__(self, equipment="bodyweight", grip="standard", execution="simultaneous"):
        self.name = "Pull-Up"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps]
        self.history = []

    def train(self, date, reps, weight=None):
        for m in self.muscles:
            m.train([reps], [0] if weight is None else [weight], date)
        sets = len(reps)
        total_volume = [r * w for r, w in zip(reps, weight)]
        self.history.append({
            "date": date, "reps": reps, "weight": weight, "sets": sets, "volume": total_volume,
            "equipment": self.equipment, "grip": self.grip, "execution": self.execution
        })


class BarbellRow(Exercise):
    usual_equipment = ["barbell", "dumbbell"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Barbell Row"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps, shoulders]
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


class ShoulderPress(Exercise):
    usual_equipment = ["barbell", "dumbbell", "machine"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Shoulder Press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [shoulders, triceps]
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


class BicepCurl(Exercise):
    usual_equipment = ["dumbbell", "barbell", "cable"]

    def __init__(self, equipment="dumbbell", grip="standard", execution="simultaneous"):
        self.name = "Bicep Curl"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [biceps]
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


class TricepPushdown(Exercise):
    usual_equipment = ["cable", "band"]

    def __init__(self, equipment="cable", grip="standard", execution="simultaneous"):
        self.name = "Tricep Pushdown"
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


class Squat(Exercise):
    usual_equipment = ["barbell", "dumbbell", "machine"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Squat"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
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


class LegPress(Exercise):
    usual_equipment = ["machine"]

    def __init__(self, equipment="machine", grip="standard", execution="simultaneous"):
        self.name = "Leg Press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
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


class Lunge(Exercise):
    usual_equipment = ["dumbbell", "barbell", "bodyweight"]

    def __init__(self, equipment="dumbbell", grip="standard", execution="sequential"):
        self.name = "Lunge"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [quads, glutes, hamstrings]
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


class RomanianDeadlift(Exercise):
    usual_equipment = ["barbell", "dumbbell"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Romanian Deadlift"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [hamstrings, glutes, lower_back]
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


class HipThrust(Exercise):
    usual_equipment = ["barbell", "machine", "bodyweight"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Hip Thrust"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [glutes, hamstrings]
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


class CalfRaise(Exercise):
    usual_equipment = ["machine", "barbell", "dumbbell"]

    def __init__(self, equipment="machine", grip="standard", execution="simultaneous"):
        self.name = "Calf Raise"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [calves]
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


class PreacherCurl(Exercise):
    usual_equipment = ["barbell", "dumbbell"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Preacher Curl"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [biceps, forearms]
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


class DumbbellRow(Exercise):
    usual_equipment = ["dumbbell", "cable"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="sequential"):
        self.name = "Dumbbell Row"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [upper_back, biceps, traps]
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


class Shrugs(Exercise):
    usual_equipment = ["dumbbell", "barbell"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="simultaneous"):
        self.name = "Shrugs"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [traps]
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


class Deadlift(Exercise):
    usual_equipment = ["barbell", "dumbbell"]

    def __init__(self, equipment="barbell", grip="standard", execution="simultaneous"):
        self.name = "Deadlift"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [lower_back, glutes, hamstrings, quads]
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


class OverheadPress(Exercise):
    usual_equipment = ["dumbbell", "barbell", "machine"]

    def __init__(self, equipment="dumbbell", grip="neutral", execution="simultaneous"):
        self.name = "Overhead Press"
        self.equipment = equipment
        self.grip = grip
        self.execution = execution
        self.muscles = [shoulders, triceps]
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
        BenchPress(),
        InclineBenchPress(),
        ChestFly(),
        PullUp(),
        BarbellRow(),
        ShoulderPress(),
        BicepCurl(),
        TricepPushdown(),
        Squat(),
        LegPress(),
        Lunge(),
        RomanianDeadlift(),
        HipThrust(),
        CalfRaise(),
        PreacherCurl(),
        DumbbellRow(),
        Shrugs(),
        Deadlift(),
        OverheadPress()
    ]