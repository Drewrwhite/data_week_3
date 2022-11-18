# _Data Engineering Week 3 Code Review_

#### By _**Drew White**_

#### _Code review for week 3 of Data Engineering: Advanced Python_

## Technologies Used

- _Python_
- _Jupyter Notebooks_
- _Pytest_
- _Faker_

## Description

 _Python code review for week 3 of Data Engineering demonstrating use of a mini ETL pipeline to process a list of colors initially generated through the use of Faker. This code review also demonstrates the use of Pytest. Steps taken in code review are as follows:_ 

- _Generate list of 20 colors named `color_list` using Faker._
- _Create `remove_dups()` function to remove duplicate colors from list._
- _Use `dictionary comprehension` to convert `color_list` to dictionary named `color_dict` with keys as colors and values as the integer length of the color name._
- _Write `color_dict` to JSON._ 
- _`color_dict.json` saves to `data` folder._
- _Read `color_dict` JSON and filter back only colors with a value of 4 or more._
- _Make a file called `test_remove_dups.py` using `@pytest.mark.parametrize()` to test `remove_dups()`_

## Setup/Installation Requirements

- _Must have Python 3.7 installed_
- _Clone this with command:  `$ git clone https://github.com/Drewrwhite/data_week_3.git`_
- _In terminal, navigate to directory where repository was cloned:  `$ cd "directory"`_
- _Create venv:  `$ python3.7 -m venv venv`_
- _Activate venv:  `$ source venv/bin/activate`_
- _Install requirements:  `$ pip install -r requirements.txt`_
- _Open in VSCode:  `$ code .`_
- _In terminal input:  `$ pytest` to test `remove_dups()`_


## Tests
 
- _All tests for code were ran in `main.ipynb` file_

## Known Bugs

- _No known bugs_

## License

[MIT](./license.txt)

_If you find any issues, please reach out at: **d.white0002@gmail.com**._

Copyright (c) _2022_ _Drew White_