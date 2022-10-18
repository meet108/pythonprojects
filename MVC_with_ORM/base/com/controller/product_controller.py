import os

from flask import render_template, jsonify, request
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.product_dao import ProductDAO
from base.com.dao.subcategory_dao import SubcategoryDAO
from base.com.vo.product_vo import ProductVO
from base.com.vo.subcategory_vo import SubCategoryVO

app.config['PRODUCT_FOLDER'] = 'base/static/product_image/'


@app.route('/admin/load_product')
def load_product():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        print("category_vo_list", category_vo_list)
        return render_template('admin/addProduct.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("Ajax load category exception", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/subcategory_load_product')
def admin_ajax_subcategory_product():
    try:
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubcategoryDAO()
        subcategory_category_id = request.args.get('productCategoryId')
        print("subcategory_category_id", subcategory_category_id)
        subcategory_vo.subcategory_category_id = subcategory_category_id
        ajax_subcategory_product = subcategory_dao.view_ajax_subcategory_product(
            subcategory_vo)
        subcategory_vo_list = [i.as_dict() for i in ajax_subcategory_product]
        print(subcategory_vo_list)
        return jsonify(subcategory_vo_list)

    except Exception as ex:
        print("AJAX LOAD PRODUCT EXCEPTION")
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/insert_product', methods=['POST'])
def admin_insert_product():
    try:
        product_category_id = request.form.get('productCategoryId')
        product_subcategory_id = request.form.get('productSubcategoryId')
        product_name = request.form.get('productName')
        product_description = request.form.get('productDescription')
        product_image = request.files.get('productImage')

        product_image_name = secure_filename(product_image.filename)
        product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
        product_image.save(
            os.path.join(product_image_path, product_image_name))

        product_vo = ProductVO()
        product_dao = ProductDAO()

        product_vo.product_name = product_name
        product_vo.product_description = product_description
        product_vo.product_image_name = product_image_name
        product_vo.product_image_path = product_image_path.replace("base",
                                                                   "..")
        product_vo.product_category_id = product_category_id
        product_vo.product_subcategory_id = product_subcategory_id
        product_dao.insert_product(product_vo)
        return render_template('admin/home.html')
    except Exception as ex:
        print("admin_insert_product route exception occured>>>>>>>>>>", ex)
        return render_template('admin/error.html', ex=ex)


@app.route('/admin/view_product')
def admin_view_product():
    try:
        product_dao = ProductDAO()
        product_vo_list = product_dao.view_product()
        return render_template('admin/viewProduct.html',
                               product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_view_product route exception occured>>>>>>>>>>", ex)
        return render_template('admin/error.html', ex=ex)
