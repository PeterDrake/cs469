# Overview
This assignment gives you an opportunity to build a network for image segmentation. It involves photos of (meteorological) clouds that I worked on with Jessica Kleiss.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Cloud Segmentation
The data here are photographs of the sky taken with a device called the Total Sky Imager (TSI). The task is to segment these (after some preprocessing) 480x480 color images into four categories:
* Non-sky (e.g., part of the apparatus blocking the camera)
* Clear sky
* Thin cloud
* Thick cloud

Such image processing might be useful to researchers studying climate change, people operating solar power plants, etc.

# Setup and Trivial Network
A lot of preprocessing and other steps went into our experiments. I'm not asking you to reproduce those; I'll just give you a harness so you can train and validate your own networks on these data.

Log on to BLT and, in your home directory, make a copy of my template directory:

```commandline
cp -r /home/drake/sky_segment/ .
```

This should create a copy of the `sky_segment` directory in your own BLT home directory.

To run a trivial network, `cd ~/sky_segment/blt_job_output` and run:

```commandline
sbatch ../src/launch_train.sh
```

This may take an hour or so to run! The results will appear in `output.txt` and `error.txt` in your `blt_job_output` directory. The final validation loss should be *very roughly* 0.4, but this may vary considerably from one run to another.

# Defining Your Own Network
To define your own network:
1. Define it in a file in the `src/mmodel_architectures` directory within your copy of `sky_segment`. Use `trivial_network.py` as an example. Of course, your network will need a number of convolutional layers. Remember that, since this is a segmentation task, the input and output images need to be the same size.
2. In `src/config.py`, alter the line `NETWORK_ARCHITECTURE = 'trivial_network'`. For example, if you named your network definition file `my_net.py`, this line should be `NETWORK_ARCHITECTURE = 'my_net'`.

Now you can run your network the same way as above. Try to get the final validation loss down to around 0.2.

# Optional Challenge Problems
* Have the best validation error. The lowest two validation rates in the class get gold stars!
* Try applying the Segment Anything model to these data. I haven't tried this, so it may be a very challenging task. I'm fine with people working as a team on this if they want to tackle it.

# What to Hand In
Hand in your network definition file and the output of your run (`output.txt`).
