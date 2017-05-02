# INF5860 Oblig 2

In this assignment you will practice building deep networks in Tensorflow. It is not much code required, but
the difficulties should be to understand Tensorflow. In this assignment you will edit the files: **DeepNetwork.ipynb**,
**Batchnorm.ipynb**, **ResNet.ipynb**, **layers.py**, **networks.py**.

We know that this can be difficult, and especially with the short deadline. So if you try your best, we will
go easy on you in the evaluation.

Even though we ask you to train some models, don't spend to much time tuning the networks, before you are finished
with the rest of your assignment. Still if you models achieve bad results, it may be an indication that you
have done some mistake.

## Parts to Complete

### Part 1: DeepNetwork
The Jupyter Notebook **DeepNetwork.ipynb** will walk you through implementing a function for 2D-convolution and
a fully connected layer in tensorflow.

### Part 2: BatchNorm
**Batchnorm.ipynb** will guide you through implementing batch normalization in tensorflow.

### Part 3: ResNet
**ResNet.ipynb** will guide you through implementing a simple residual block, that can be reused for many applications.

## Get Started
Download the starter code from git with:

    git clone https://github.com/sigmunjr/INF5860_oblig2.git

**[Option 1] Use IFI-linux computer:**

If you have not installed Jupyter on you IFI-computer, you can run it with:

    /hom/sigmunjr/anaconda/bin/jupyter notebook

Instead of just `jupyter notebook`. Otherwise everything **should** work fine.

**[Option 2] Use Anaconda:**
The preferred approach for installing all the assignment dependencies is to use
[Anaconda](https://www.continuum.io/downloads), which is a Python distribution
that includes many of the most popular Python packages for science, math,
engineering and data analysis. Once you install it you can skip all mentions of
requirements and you are ready to go directly to working on the assignment.

**[Option 3] Manual install, virtual environment:**
If you do not want to use Anaconda and want to go with a more manual and risky
installation route you will likely want to create a
[virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
for the project. If you choose not to use a virtual environment, it is up to you
to make sure that all dependencies for the code are installed globally on your
machine. To set up a virtual environment, run the following:

```bash
cd INF5860_oblig2
sudo pip install virtualenv      # This may already be installed
virtualenv .env                  # Create a virtual environment
source .env/bin/activate         # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies
# Work on the assignment for a while ...
deactivate                       # Exit the virtual environment
```

**Download data:**
Once you have the starter code, you will need to download the CIFAR-10 dataset.
Run the following from the `INF5860_oblig2` directory:

```bash
cd datasets
./get_datasets.sh
```


**Start Jupyter:**
After you have the CIFAR-10 data, you should start the **jupyter notebook** server
from the `INF5860_oblig2` directory. In the `INF5860_oblig2` directory run:

    jupyter notebook
    
Then you will se the list of the notebooks, that should be solved in the provided order: **softmax.ipynb**, **two_layer_net.ipynb**, **features.ipynb** and **backpropagation_network.ipynb**.
By clicking on a notebook, you can start working on an assignment. You can run a cell with `shift+enter` or `ctrl+enter`. You can find more
keyboard shortcuts [here](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/).

If you are unfamiliar with jupyter, you can test it out with [try Jupyter](https://try.jupyter.org/). There you can find a simple overview
in the `Welcome to Python.ipynb` notebook. To get a more extensive guide you can go to `communities/pyladies/Python 101.ipynb`.



### Submitting your work:
Whether you work on the assignment locally or using Terminal, once you are done
working run the `collectSubmission.sh` script; this will produce a file called
`INF5860_Oblig1.zip`. 
