# add_slide.py

動画作成に使用するスライド用の作業ディレクトリを作成し、テンプレートファイルを用意する。

## 使い方

```shell
% ~/bin/add_slide -h
usage: add_slide [-h] [-s SLIDE_DIR] [--with-code] [--without-code] [--template-dir TEMPLATE_DIR] [-t {default,short}] PROJECT_NAME

動画作成用のスライドプロジェクトを作成しvscodeで開く。もし既に存在するプロジェクトの場合はそのプロジェクトをvscodeで開く。

positional arguments:
  PROJECT_NAME          プロジェクト名

options:
  -h, --help            show this help message and exit
  -s SLIDE_DIR, --slide-dir SLIDE_DIR
                        スライドプロジェクトのルートディレクトリ。(デフォルト値: ~/slide)
  --with-code           VScodeでプロジェクトを開く。
  --without-code        VScodeでプロジェクトを開かない。
  --template-dir TEMPLATE_DIR
                        プロジェクトを新規作成時に雛形とするディレクトリ。(デフォルト値: ~/opt/add_slide/template)
  -t {default,short}, --template-name {default,short}
                        テンプレート名。(デフォルト値: default)
```

デフォルトテンプレートでスライドを作成する場合、

```shell
% ~/bin/add_slide.py test01
```

ショート動画用テンプレートでスライドを作成する場合、

```shell
% ~/bin/add_slide.py -t short test01
```

## インストール

```shell
make install
```

## アンインストール

```shell
make clean
```
