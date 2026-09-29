from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

# ---------------- ALUMNI DATA ----------------

ALUMNI = [
    {
        "id": 1,
        "name": "Aarav Kumar",
        "email": "aarav.kumar@example.com",
        "graduation": "B.Tech CSE, 2022",
        "company": "TechNova Solutions",
        "role": "Software Engineer",
        "location": "Hyderabad",
        "skills": "Python, Flask, SQL, AWS",
        "experience": "3 years",
        "bio": "Software engineer interested in backend development, cloud technologies and mentoring students.",
        "achievements": "Built scalable web applications and mentored junior developers."
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "graduation": "B.Tech CSE, 2021",
        "company": "Deloitte",
        "role": "Business Technology Analyst",
        "location": "Bengaluru",
        "skills": "SQL, Data Analytics, Power BI",
        "experience": "4 years",
        "bio": "Technology professional who enjoys helping students understand careers in IT consulting and analytics.",
        "achievements": "Worked on enterprise analytics and business technology projects."
    },
    {
        "id": 3,
        "name": "Rahul Reddy",
        "email": "rahul.reddy@example.com",
        "graduation": "B.Tech CSE, 2020",
        "company": "Infosys",
        "role": "DevOps Engineer",
        "location": "Hyderabad",
        "skills": "AWS, Linux, Docker, Jenkins",
        "experience": "5 years",
        "bio": "Cloud and DevOps professional offering guidance on cloud careers, projects and interview preparation.",
        "achievements": "Automated deployment workflows and supported cloud infrastructure projects."
    },
    {
        "id": 4,
        "name": "Sneha Patel",
        "email": "sneha.patel@example.com",
        "graduation": "B.Tech IT, 2023",
        "company": "Amazon",
        "role": "Data Analyst",
        "location": "Chennai",
        "skills": "Python, Pandas, SQL, Tableau",
        "experience": "2 years",
        "bio": "Data analyst focused on data-driven decision making and career mentoring.",
        "achievements": "Created dashboards and analytics solutions for business teams."
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "email": "vikram.singh@example.com",
        "graduation": "B.Tech CSE, 2019",
        "company": "Microsoft",
        "role": "Cloud Engineer",
        "location": "Pune",
        "skills": "Azure, Python, Kubernetes, Terraform",
        "experience": "6 years",
        "bio": "Cloud engineer interested in infrastructure, automation and helping students prepare for cloud roles.",
        "achievements": "Worked on cloud migration and infrastructure automation projects."
    }
]


# ---------------- ALUMNI SPEAKS ----------------

SPEAKS = [
    {
        "id": 1,
        "title": "Building a Career in Technology",
        "author": "Aarav Kumar",
        "content": "Tips on backend development, projects and preparing for software engineering careers."
    },
    {
        "id": 2,
        "title": "From College to IT Consulting",
        "author": "Priya Sharma",
        "content": "Guidance for students interested in consulting, analytics and technology careers."
    },
    {
        "id": 3,
        "title": "Getting Started with Cloud and DevOps",
        "author": "Rahul Reddy",
        "content": "An alumni perspective on cloud technologies, DevOps skills and interview preparation."
    }
]


# ---------------- WEBINARS ----------------

WEBINARS = [
    {
        "title": "Career Opportunities in Software Engineering",
        "speaker": "Aarav Kumar",
        "date": "15 October 2026",
        "description": "A session on software development careers, projects and interview preparation."
    },
    {
        "title": "Cloud and DevOps Career Roadmap",
        "speaker": "Rahul Reddy",
        "date": "22 October 2026",
        "description": "An interactive webinar covering cloud, Linux, Docker and DevOps fundamentals."
    }
]


# ---------------- QUESTIONS ----------------

QUESTIONS = []


# ---------------- EVENTS ----------------

EVENTS = [
    {
        "title": "Alumni Reunion",
        "type": "Reunion",
        "date": "December 2026",
        "description": "Annual alumni reunion for connecting graduates, students and faculty."
    },
    {
        "title": "Alumni Achievement Meet",
        "type": "Alumni Achievement",
        "date": "November 2026",
        "description": "Celebrating achievements and professional contributions of alumni."
    },
    {
        "title": "College Achievement Celebration",
        "type": "College Achievement",
        "date": "December 2026",
        "description": "Celebrating academic and extracurricular achievements of the college community."
    }
]


# ---------------- REFERENCES ----------------

REFERENCES = {
    "notes": [
        "Career preparation notes",
        "Programming and technical interview resources",
        "Project development guidance"
    ],
    "sports": [
        "College sports activities",
        "Alumni sports achievements",
        "Sports reunion activities"
    ],
    "higher_studies": [
        "Higher studies guidance",
        "Postgraduate opportunities",
        "Alumni experiences with higher education"
    ]
}


# ---------------- REGISTERED USERS ----------------

USERS = []


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template(
        "index.html",
        featured=ALUMNI[:3]
    )


# =========================================================
# ABOUT
# =========================================================

@app.route("/about")
def about():
    return render_template("about.html")


# =========================================================
# ALUMNI DIRECTORY
# =========================================================

@app.route("/alumni")
def alumni_directory():

    search = request.args.get("search", "").strip().lower()

    results = ALUMNI

    if search:
        # Allow comma-separated or space-separated searches
        keywords = [
            word.strip()
            for word in search.replace(",", " ").split()
            if word.strip()
        ]

        results = []

        for person in ALUMNI:

            searchable_text = " ".join([
                str(person.get("name", "")),
                str(person.get("role", "")),
                str(person.get("company", "")),
                str(person.get("location", "")),
                str(person.get("skills", ""))
            ]).lower()

            # Match if ANY entered keyword is found
            if any(keyword in searchable_text for keyword in keywords):
                results.append(person)

    return render_template(
        "alumni_directory.html",
        alumni=results,
        search=search
    )


# =========================================================
# ALUMNI DETAILS
# =========================================================

@app.route("/alumni/<int:alumni_id>")
def alumni_details(alumni_id):

    person = next(
        (p for p in ALUMNI if p["id"] == alumni_id),
        None
    )

    if not person:
        abort(404)

    return render_template(
        "alumni_detail.html",
        person=person
    )


# =========================================================
# CONNECT WITH ALUMNI
# =========================================================

@app.route("/connect/<int:alumni_id>", methods=["GET", "POST"])
def connect(alumni_id):

    person = next(
        (p for p in ALUMNI if p["id"] == alumni_id),
        None
    )

    if not person:
        abort(404)

    submitted = request.method == "POST"

    return render_template(
        "connect.html",
        person=person,
        submitted=submitted
    )


# =========================================================
# ALUMNI SPEAKS
# =========================================================

@app.route("/alumni-speaks")
def alumni_speaks():

    return render_template(
        "alumni_speaks.html",
        speaks=SPEAKS,
        webinars=WEBINARS
    )


# =========================================================
# WEBINARS
# =========================================================

@app.route("/webinars")
def webinars():

    return render_template(
        "webinars.html",
        webinars=WEBINARS
    )


# =========================================================
# ALUMNI ASSISTANCE / ASK QUESTION
# =========================================================

@app.route("/assistance", methods=["GET", "POST"])
def assistance():

    submitted = False

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        question = request.form.get("question", "").strip()

        if name and question:

            QUESTIONS.append({
                "name": name,
                "question": question
            })

            submitted = True

    return render_template(
        "assistance.html",
        questions=QUESTIONS,
        submitted=submitted
    )


# =========================================================
# EVENTS
# =========================================================

@app.route("/events")
def events():

    return render_template(
        "events.html",
        events=EVENTS
    )


# =========================================================
# REFERENCES
# =========================================================

@app.route("/references")
def references():

    return render_template(
        "references.html",
        references=REFERENCES
    )


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    registered = False

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if name and email and password:

            USERS.append({
                "name": name,
                "email": email,
                "password": password
            })

            registered = True

    return render_template(
        "register.html",
        registered=registered
    )


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        user = next(
            (
                u for u in USERS
                if u["email"] == email
                and u["password"] == password
            ),
            None
        )

        if user:
            message = f"Welcome, {user['name']}!"
        else:
            message = "Invalid email or password."

    return render_template(
        "login.html",
        message=message
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)