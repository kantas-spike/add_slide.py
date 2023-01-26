# add_slide.py

動画作成に使用するスライド用の作業ディレクトリを作成し、テンプレートファイルを用意する。

## 使い方

```shell
% ~/bin/add_slide.py -h
usage: add_slide.py [-h] [--root-dir ROOT_DIR] [--with-code] [--without-code] [--template-dir TEMPLATE_DIR] PROJECT_NAME

動画作成用のスライドプロジェクトを作成しvscodeで開く。もし既に存在するプロジェクトの場合はそのプロジェクトをvscodeで開く。

positional arguments:
  PROJECT_NAME          プロジェクト名

options:
  -h, --help            show this help message and exit
  --root-dir ROOT_DIR   スライドプロジェクトのルートディレクトリ。(デフォルト値: ~/slide)
  --with-code           VScodeでプロジェクトを開く。
  --without-code        VScodeでプロジェクトを開かない。
  --template-dir TEMPLATE_DIR
                        プロジェクトを新規作成時に雛形とするディレクトリ。(デフォルト値: ~/opt/add_slide/template/default/)
```

```shell
% ~/bin/add_slide.py test01
mkdir /Users/kanta/slide/05_test01/ ...
copytree /Users/kanta/opt/add_slide/template/default/slide /Users/kanta/slide/05_test01/slide ...
copyfile /Users/kanta/opt/add_slide/template/default/description.md /Users/kanta/slide/05_test01/description.md ...
code /Users/kanta/slide/05_test01/ ...
```

## インストール

```shell
make install
```

## アンインストール

```shell
make clean
```