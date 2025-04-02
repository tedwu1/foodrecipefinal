from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

def new_func(app):
    app.run(debug=True)

if __name__ == "__main__":
    new_func(app)