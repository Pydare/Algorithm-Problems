s = """
    ## Dependency
    - Python3, Ubuntu 18.04 or WindowsOS
    - OpenCV, Tensorflow, Keras, Pillow
    - To install the required packages, run pip install -r requirements.txt
    """

s = s.split('\n')
print(s)

def parse_to_html(s):
    
    s = s.split('\n')

    for sentence in s:
        convert_to_html(sentence)
    
    return s

def convert_to_html(s):

    markdown_html = {'#':'<h1>', '-':'<li>'}