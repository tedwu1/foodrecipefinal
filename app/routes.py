from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Recipe
from app.forms import RecipeForm

main = Blueprint("main", __name__)

@main.route("/")
def home():
    recipes = Recipe.query.all()
    return render_template("home.html", recipes=recipes)

@main.route("/recipe/new", methods=["GET", "POST"])
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for("main.home"))
    return render_template("new_recipe.html", form=form)

@main.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe_detail.html", recipe=recipe)

@main.route("/recipe/<int:recipe_id>/delete", methods=["POST"])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted!", "danger")
    return redirect(url_for("main.home"))
