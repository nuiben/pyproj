import csv
from faker import Faker
import random

fake = Faker()

# Define some constants for the data generation
NUM_RECORDS = 20000
STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

FIRST_NAMES = [
    'Joe', 'Sue', 'Charlie', 'Beth', 'Andre', 'LeAnna', 'Rick', 'Wendy',
    "James", "Emma", "Paul", "Richard", "Aaliyah", "Carlos", "Fatima", "Deepak",
    "Elena", "Hiroshi", "Isra", "Jamar", "Kyung", "Lakisha", "Mohammed", "Naveen",
    "Oluchi", "Pablo", "Qasim", "Rashida", "Sandeep", "Tariq", "Usha", "Vinh",
    "Wan", "Xiu", "Yasmin", "Zanele", "Aditi", "Bao", "Chen", "Dalia", "Eshe", "Fernando"
]

LAST_NAMES = [
    "Nguyen", "Patel", "Kim", "Gomez", "Khan", "Wang", "Alonso", "Mbatha",
    "Smith", "Rodriguez", "Goldberg", "Narayan", "Brown", "Okoye", "Takashi",
    "Jackson", "Mutombo", "Singh", "Chavez", "Abdullah", "Okafor", "Naidu",
    "Lee", "Lopez", "Gupta", "Ali", "Tsai", "Zimmerman", "Bello", "O'Reilly", "Smith", "Rogers"
]



PHYSICAL_ACTIVITY = ["Highly Active", "Active", "Moderate", "Light", "Sedentary"]  # Add as many health indicators as required
TRUTHY = [True, False]
POPULATION_GROUPS = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]  # Add population groups
DIET = ["Good", "Fair", "Poor"]
BLOOD_PRESSURE = ["Normal", "Elevated", "Stage 1 Hypertension", "Stage 2 Hypertension"]
# Open a new CSV file for writing
with open("national_survey.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "State_ID", "State", "County ID","Physical Activity", "Tobacco Use","Diet","Blood Pressure", "Population Group", "Value"])  # Writing headers

    # Generate fake data
    for _ in range(NUM_RECORDS):
        state = random.choice(STATES)
        state_id = STATES.index(state) + 1
        county_id = random.randint(1, 62);
        name = f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}';
        phys_activity = random.choice(PHYSICAL_ACTIVITY)
        tobacco_use = random.choice(TRUTHY)
        diet = random.choice(DIET)
        systolic_bp = random.randint(100, 250)
        dystolic_bp = systolic_bp - random.randint(40, 60)
        blood_pressure = str(systolic_bp) + "/" + str(dystolic_bp)
        pop_group = random.choice(POPULATION_GROUPS)
        value = random.randint(10, 500)  # Random integer value for health indicator

        writer.writerow([name, state_id, state, county_id, phys_activity, tobacco_use, diet, blood_pressure, pop_group, value])

print(f"Generated {NUM_RECORDS} fake records in national_survey.csv.")
