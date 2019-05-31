# Test task for comparing pictures dataset


## Requirements

- Python 3
- Pillow

See more in `requirements.txt`

## How to use

To start script execute following

```sh
python solution.py ./dataset
```

### Examples

```sh
$ python solution.py 
usage: solution.py [-h] --path PATH
solution.py: error: the following arguments are required: --path
```

```sh
$ python solution.py -h
usage: solution.py [-h] --path PATH

The test task on images similarity

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  folder with images
```

```sh
python solution.py --path ./dataset
Duplicate:
('11_duplicate.jpg', '11.jpg')
('1.jpg', '1_duplicate.jpg')
Modification:
('11_duplicate.jpg', '11_modification.jpg')
('15.jpg', '15_modification.jpg')
('11.jpg', '11_modification.jpg')
Supposed to be similar:
('6_similar.jpg', '6.jpg')
('4.jpg', '4_similar.jpg')

```


