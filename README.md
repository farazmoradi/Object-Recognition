# Computer Vision Project

<div style="text-align: justify">

In this project, we utilized Detectron2 to automate the process of sky removal in a selected subset of images from the COCO dataset. Our approach focused on advanced image processing techniques to identify and exclude the sky regions, allowing for further analysis and use of the sky-free images.

* **Task 1:** Selecting a subset of images which contain sky (12 images).
* **Task 2:** Instance Segmentation on the selected images using Detectron2.
* **Task 3:** Automatically identifying sky regions in images and subsequently removing these regions to generate sky-free images.
* **Task 4:** Visualizations to compare the original images with sky-free images.

# How to run the project


1. Download the source code:
> $ git clone https://github.com/farazmoradi/Object-Recognition.git
2. In the notebooks folder, open the **CV_project.ipynb** to see the project. 
3. Start running the cells and enjoy!

# Dependencies

* To run the code, you need to have PyTorch, Detectron2, and PIL (Pillow) installed in your Python environment. If not already installed, you can add them using pip.

> pip install torch torchvision

> python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

> pip install pillow

* If CUDA is available on your system, this notebook will automatically detect it and execute operations on the GPU for improved performance.

</div>
