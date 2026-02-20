from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple career recommendations data
career_data = {
    "data science": {
        "skills": ["Python", "Statistics", "Machine Learning", "SQL"],
        "roadmap": "Learn Python → Learn Statistics → Explore ML → Work on projects"
    },
    "web development": {
        "skills": ["HTML", "CSS", "JavaScript", "Flask/Django"],
        "roadmap": "Learn HTML/CSS → Learn JS → Learn Flask/Django → Build portfolio"
    },
    "ai engineer": {
        "skills": ["Python", "Deep Learning", "TensorFlow/PyTorch", "Math"],
        "roadmap": "Learn Python → Study Deep Learning → Work with TensorFlow/PyTorch → Projects"
    },
    "digital marketing": {
        "skills": ["SEO", "Content Marketing", "Social Media", "Analytics"],
        "roadmap": "Learn SEO → Content Marketing → Social Media strategies → Analytics tools"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["message"].lower()
    response = "Sorry, I don't have information about that career yet."
    
    for career in career_data:
        if career in user_input:
            skills = ", ".join(career_data[career]["skills"])
            roadmap = career_data[career]["roadmap"]
            response = f"Career: {career.title()}\nRequired Skills: {skills}\nLearning Roadmap: {roadmap}"
            break
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
