@app.route('/test-image')
def test_image():
    """Test page for troubleshooting image loading issues"""
    return render_template('test-image.html')