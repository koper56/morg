<img aligh="left" src="https://camo.githubusercontent.com/c2ed0c1d8ac1a5ebbe7281923d42b50b7962912c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e362d626c75652e737667"/>


morg - My Organiser
===================
<img align="right" height="250" src="http://i.imgur.com/0yPtcWq.png"/>

_My first project, started on February 9th 2017._


Description
-----------
_Put your wardrobe to python!_


App for manage clothes and sets of clothes. 
 - search (by name, kind, rate, sets)
 - rate (1 - 5)
 - add (with name, description, exclusions, rate, clear, photo, colors and kind)
 - change
 - delete 
 - check weather for now, + 3h, + 6h, +9h 

Required
--------
Module                                                     | Version
-------                                                    |--------
[Cyton](http://cython.org/)	                               |_0.25.2_
[Pygame](https://www.pygame.org/)                          |_1.9.3_
[Kivy](https://kivy.org/)                                  |_1.10.0_
[Requests](http://docs.python-requests.org/)               |_2.14.2_
[SQLAlchemy](https://sqlalchemy.org)                       |_1.1.9_
[opencv-python](https://pypi.python.org/pypi/opencv-python)|_3.2.0.7_

> **NOTE:** You can generate your own weather API token:
>- [Weather API](https://www.wunderground.com)
>- Put your API token to _WUNDERGROUND_API_TOKEN_ in _morg/weather.py_

How to use
----------

    git clone https://github.com/mkopr/morg.git (or manually download)
    cd morg
    pip install Cython (temporary solve install problem)
    pip install -e .
    morg
    
    
For virtualenv:

    git clone https://github.com/mkopr/morg.git (or manually download)
    cd morg
    mkvirtualenv -a <morg dir> -p python3 morg
    pip install Cython (temporary solve install problem)
    pip install -e .
    morg


    
In first run app create file _weatherdata.txt_ with weather info from _weather.py_.

In first run app create _data_base_file.db_ with two tables: _ClothesData_ and _HistoryData_.

App crate _morg_RRRR_MM_DD.log_ file in ./logs with logging info. 

Store clothes photos (png files) in ./photo.

Store sets photos (png files) in ./sets.

Store png files used in app in ./assets/images.


Screens
-------
Few screens from app:


<img align="left" height="300" src="http://i.imgur.com/ch37U7V.png"/>
<img align="right" height="300" src="http://i.imgur.com/CQRaV82.png"/>

<img align="left" height="300" src="http://i.imgur.com/PQldAEC.png"/>
<img align="right" height="300" src="http://i.imgur.com/WIN5qXO.png"/>

<img align="left" height="300" src="http://i.imgur.com/yok3Pf2.png"/>
<img align="right" height="300" src="http://i.imgur.com/tcJbgRt.png"/>

<img align="left" height="300" src="http://i.imgur.com/fqVybrJ.png"/>
