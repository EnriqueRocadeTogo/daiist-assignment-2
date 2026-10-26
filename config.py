"""
Every decision this project depends on, in one place.

train.py, costing.py and app.py all read these values, so each number lives in
exactly one spot. The business figures in sections 4 and 5 are your own
judgement: each one needs a reason and a source in REPORT.md, plus a sentence on
what would change if it were wrong.

While PLACEHOLDERS is True the dashboard shows a warning banner. Set it to False
once every TODO below holds a figure you can defend.
"""

# 1. The decision -------------------------------------------------------------
# One or two sentences: what is decided, by whom, from which image.
DECISION = "TODO: describe the decision the model supports and who acts on it."

# What a positive case is called on screen, e.g. "defect" or "violation".
POSITIVE_NAME = "rotten fruit"

# A case is one image. It is POSITIVE when it contains at least one object of
# any of these classes. Use the dataset's class names exactly as published.
POSITIVE_CLASSES: list[str] = ["rotten"]   # your call: add "overripe" if that also triggers the action
# Classes in this dataset: freshripe, freshunripe, overripe, ripe, rotten, unripe

# 2. The dataset: Roboflow Universe, used as published, never forked ----------
# Read them off the URL: universe.roboflow.com/<workspace>/<project>/dataset/<version>
ROBOFLOW_WORKSPACE = "fruit-ripening"
ROBOFLOW_PROJECT = "fruit-ripening-process"
ROBOFLOW_VERSION = 1   # "raw": 5,264 train / 1,525 valid / 757 test, no augmentation

# 3. Training ------------------------------------------------------------------
BASE_MODEL = "yolo11n.pt"   # pretrained on COCO; "yolo11s.pt" is bigger and slower
EPOCHS = 50
IMAGE_SIZE = 640
BATCH = 16
PATIENCE = 15               # stop early after this many epochs without improvement
SEED = 0
DEVICE = "auto"             # "auto" = NVIDIA GPU if present, else CPU. "mps" on an Apple Silicon Mac.
WHERE_TRAINED = "TODO: e.g. Google Colab, NVIDIA T4"

# COCO zero-shot baseline. A COCO class whose name equals one of your classes is
# matched automatically. To let a COCO class stand in for one of yours, add it as
# {"your_class": ["coco_class"]} and defend that choice in REPORT.md.
COCO_STAND_INS: dict[str, list[str]] = {}

# 4. The cost of being wrong, in euros per case --------------------------------
# TODO: every figure in this section and the next is a placeholder.
COST_FALSE_POSITIVE = 1.0   # the model flags a case that was fine
COST_FALSE_NEGATIVE = 1.0   # the model passes a case that was not fine
COST_TRUE_POSITIVE = 0.0    # cost of acting on a correct flag, if there is one
COST_TRUE_NEGATIVE = 0.0
BASE_RATE = 0.10            # share of real-world cases that are positive

# 5. Human review --------------------------------------------------------------
CASES_PER_DAY = 1_000
SECONDS_PER_REVIEW = 10
REVIEWER_COST_PER_HOUR = 25.0          # fully loaded cost of a reviewer's hour
PRODUCTIVE_HOURS_PER_REVIEWER = 7.0    # per reviewer per day
REVIEWERS_AVAILABLE = 1.0              # people you could actually put on review

PLACEHOLDERS = True
