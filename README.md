# Total Watch Duration
Python script to calculate total duration of video files in a directory.

# What this does
I made this script mainly because whenever I download tutorials or TV show episodes to watch them offline, I needed a utility that would tell me the total duration of the entire video series.

# Prerequisites
Make sure you have [FFmpeg](https://ffmpeg.org/download.html) installed at `/usr/local/bin/ffmpeg`. If it's in a different location, make sure to change [line #17](src.py#L17) to point to the right location of the binary.

# Usage: As Script
1. Download the [main script file](src.py).
2. Open a Terminal window and type **python src.py <path-to-target-folder>**.

# Usage: As Automator Service

1. Open **Applications -> Automator**.
2. Select **File -> New** in the menu bar.
3. Chose the document type as **Service**.
![Screenshot of choosing document type as service](https://i.imgur.com/suc88tq.png)
4. Within the right pane's top panel, choose **files or folders** from the first dropdown and then **Finder.app** from the second dropdown.
5. Within the left actions pane, select **Run Shell Script**.
![Screenshot of selecting run shell script](https://i.imgur.com/kNsJdhq.png)
6. When the Run Shell Script box appears in the right pane, change the **Shell** value to **/usr/bin/python** and the **Pass input** value to **to arguments**.
7. Now paste [the contents of src.py](src.py) into that script box. It should look like this:
![Screenshot of Run Shell Script box](https://i.imgur.com/wCkuIjD.png)
8. Finally click **File -> Save** in the menu bar to save the Automator task.  The name you save the task as is what will display at the context menu name.
9. You can close Automator now as it would have installed the service to your laptop.
10. On right clicking on a folder, the service should appear and you can click on it to get the total duration of all the video files inside it _including the ones within sub-folders_.
![Screenshot of the context menu](https://i.imgur.com/9OkukDv.png).

# Contributing
If you have a better way of using this or have code improvements feel free to make a PR to my repository. I will verify it and if it's good, I'll integrate it in. Enjoy!
