#!/usr/bin/env python3

import argparse
import os
import re
import shutil
import glob
import sys


def find_dir_with_numberprefix(
    name_without_numberprefix, root_dir, prefix_separator="_"
):
    ab_root_dir = expand_path(root_dir)
    max_no = 0
    match_dir = None
    for d in glob.glob(os.path.join(ab_root_dir, f"*{prefix_separator}*/")):
        dname = os.path.basename(os.path.dirname(d))
        pattern = re.compile(r"(\d+)%s(.*)\Z" % re.escape(prefix_separator))
        if m := re.match(pattern, dname):
            if m[2] == name_without_numberprefix:
                match_dir = d
                break
            no = int(m[1])
            if max_no < no:
                max_no = no

    if match_dir:
        return match_dir
    else:
        return os.path.join(
            ab_root_dir,
            f"{max_no + 1:02}{prefix_separator}{name_without_numberprefix}/",
        )


def get_template_path(template_root, template_name):
    return expand_path(os.path.join(template_root, template_name))


def main():
    args = parse_args()
    dpath = find_dir_with_numberprefix(args.project_name, args.slide_dir)

    if not os.path.isdir(dpath):
        print(f"mkdir {dpath} ...")
        os.makedirs(dpath)
        tpath = get_template_path(args.template_dir, args.template_name)
        print(f"template dir({tpath})...")
        if os.path.isdir(tpath):
            for i in glob.glob(os.path.join(tpath, "*")):
                bname = os.path.basename(i)
                dst_path = os.path.join(dpath, bname)
                if os.path.isdir(i):
                    print(f"copytree {i} {dst_path} ...")
                    shutil.copytree(i, dst_path)
                else:
                    print(f"copyfile {i} {dst_path} ...")
                    shutil.copyfile(i, dst_path)
        else:
            print(f"template dir({tpath})は存在しません!!")

    if args.with_code:
        print(f"code {dpath} ...")
        os.system(f"code '{dpath}'")


def expand_path(path):
    return os.path.abspath(os.path.expanduser(path))


def parse_args():
    DEFAULT_ROOT_DIR = "~/slide"
    DEFAULT_TEMPLATE_DIR = "~/opt/add_slide/template"
    DEFAULT_TEMPLATE_NAME = "default"
    parser = argparse.ArgumentParser(
        description="動画作成用のスライドプロジェクトを作成しvscodeで開く。"
        "もし既に存在するプロジェクトの場合はそのプロジェクトをvscodeで開く。"
    )
    parser.add_argument(
        "project_name", metavar="PROJECT_NAME", type=str, help="プロジェクト名"
    )
    parser.add_argument(
        "-s",
        "--slide-dir",
        type=str,
        default=DEFAULT_ROOT_DIR,
        help=f"スライドプロジェクトのルートディレクトリ。(デフォルト値: {DEFAULT_ROOT_DIR})",
    )
    parser.add_argument(
        "--with-code",
        dest="with_code",
        default=True,
        action="store_true",
        help="VScodeでプロジェクトを開く。",
    )
    parser.add_argument(
        "--without-code",
        dest="with_code",
        action="store_false",
        help="VScodeでプロジェクトを開かない。",
    )
    parser.add_argument(
        "--template-dir",
        default=DEFAULT_TEMPLATE_DIR,
        help=f"プロジェクトを新規作成時に雛形とするディレクトリ。(デフォルト値: {DEFAULT_TEMPLATE_DIR})",
    )

    parser.add_argument(
        "-t",
        "--template-name",
        default=DEFAULT_TEMPLATE_NAME,
        choices=[DEFAULT_TEMPLATE_NAME, "short"],
        help=f"テンプレート名。(デフォルト値: {DEFAULT_TEMPLATE_NAME})",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    sys.exit(main())
