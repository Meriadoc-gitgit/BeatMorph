# music-genre-classification

## Activate virtual environment
```shell
conda create --name beatmorph python=3.9
conda activate beatmorph
```
### Install all requirements
```shell
conda install pip
pip install -r requirements.txt
```

### Extract data
```shell
python -m bin.extract_data --data_path /Users/vuhoangthuyduong/Documents/music-genre-classification/data/genres_original --output_dir /Users/vuhoangthuyduong/Documents/music-genre-classification/data/features_waves
```