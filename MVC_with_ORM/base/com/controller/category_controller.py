from flask import render_template, request, redirect

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route('/')
def load_homepage():
    try:
        return render_template("admin/home.html")
    except Exception as ex:
        print("Homepage exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/load_category')
def admin_load_category():
    try:
        return render_template("admin/addCategory.html")
    except Exception as ex:
        print("Load category exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/insert_category', methods=['POST'])
def admin_insert_category():
    try:
        category_name = request.form.get('categoryName')
        category_description = request.form.get('categoryDescription')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.insert_category(category_vo)
        return render_template("admin/home.html")
    except Exception as ex:
        print("Insert Category Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/view_category', methods=['GET'])
def admin_view_category():
    try:
        category_dao = CategoryDAO()
        category_dao.view_category()
        return render_template("admin/viewCategory.html",
                               category_vo_list=category_dao.view_category())
    except Exception as ex:
        print("View Category Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/delete_category', methods=['GET'])
def admin_delete_category():
    try:
        category_id = request.args.get('categoryId')
        category_vo = CategoryVO()
        category_vo.category_id = category_id

        category_dao = CategoryDAO()
        category_dao.delete_category(category_vo)
        return redirect('/admin/view_category')

    except Exception as ex:
        print("Delete Category Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/edit_category', methods=['GET'])
def admin_edit_category():
    try:
        category_id = request.args.get('categoryId')
        category_vo = CategoryVO()
        category_vo.category_id = category_id

        category_dao = CategoryDAO()
        category_vo_list = category_dao.edit_category(category_vo)
        return render_template("admin/editCategory.html",
                               data=category_vo_list)
    except Exception as ex:
        print("Edit Category Exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/update_category', methods=['POST'])
def admin_update_category():
    try:
        category_id = request.form.get('categoryId')
        CategoryName = request.form.get('categoryName')
        Description = request.form.get('categoryDescription')
        category_vo = CategoryVO()
        category_vo.category_id = category_id
        category_vo.category_name = CategoryName
        category_vo.category_description = Description
        category_dao = CategoryDAO()
        category_dao.update_category(category_vo)
        return redirect('/admin/view_category')

    except Exception as ex:
        print("Update Category Exception", ex)
        return render_template('admin/error.html', ex=ex)
