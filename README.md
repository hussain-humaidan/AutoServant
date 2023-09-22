<center><img alt="Coding" width="400" src="https://cdn.dribbble.com/users/1162077/screenshots/3848914/programmer.gif"></center>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/hussain-humaidan-a5a515216/" target="blank"><img align="center" src="https://gist.githubusercontent.com/Cytancy/d1e4a0f0edc874092613ddaef897b2a6/raw/a9b4317a94a7fd6706d20a5a018d028a333b83a6/linkedin.svg" alt="kalpeshofficial" height="30" width="40" /></a>
<a href="https://www.youtube.com/@hybrid-technology" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="kalpesh144d" height="30" width="40" /></a>
<a href="https://www.instagram.com/pycode_hub" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="_kalpesh__official_" height="30" width="40" /></a>
</p>

# Goal

This script goal is for automating local files from the source to a destination. **(destination is located on a remote server)**

We will be using Python script with lib ‘ftplib’, since we have already successfully attempted to connect with remote server via SSH.

# Code working steps

1.  The code will get into all DIR's in the [path provided](https://github.com/hussain-creator/AutoServant/blob/edad58fcde5431c06994b07119ec2f4be01efe71/main.py?plain=1#L22), and will look up for [file.txt](https://github.com/hussain-creator/AutoServant/blob/main/fottage/file.txt).
2.  The code will read the file.txt data as shown below:
    - file_name: \<file_name>
    - event_date: \<event_date>, <ins>keep the simple format: 15-5-2020</ins>
    - name_of_lecturer: \<name_of_lecturer>
    - other_lecturers: \<other_lecturers>
    - event_type: \<event_type>
3.  From the given concrete file, we will create directories with the following pattern:
    &rarr; Gregorian year - Hijri year
    <br/>
    &nbsp;&nbsp;&rarr; Gregorian month - Hijri month
    <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&rarr; Event type
    <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&rarr; File name
4.  If directory exists, the code will change its current directory to the specified location within it.
5.  If duplicated files exists, in other words files \<file_name> exists twice,the code will add tag \<file_name>\_2 **automatically**.

# Example

Let’s say we have been given a file with the following data:

- file_name: *The Quantum Dynamics*
- event_date: *16-5-2023*
- name_of_lecturer: *Mohammed Hassan*
- other_lecturers: *Ali Hussain*
- event_type: *Scientific conference*

## Expected output:

&rarr; year_2019 - hijri_1440
<br/>
&nbsp;&nbsp;&rarr; month_5 - month_hijri_9
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&rarr; Scientific conference
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&rarr; The Quantum Dynamics
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&rarr; :star: Contents

# Running the code
```commandline
$ git clone {link_Here}
$ cd {DIR_NAME}
$ pip3 install requirments.txt
$ python3 main.py
```
> To ensure compatibility, use the pip command that corresponds to the same version of Python. For example: for Python 3, use pip3, and for Python 2, use pip.

# Additional resources

python ftplib: https://docs.python.org/3/library/ftplib.html <br />
You can use this endpoint to fetch hijri dates: http://api.aladhan.com/v1/gToH/11-5-2023

