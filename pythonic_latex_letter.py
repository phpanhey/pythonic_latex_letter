import argparse
import json
import os


def main():
    config = get_config()
    populated_latex_markup = populate_latex_src(config)
    compile_pdf(populated_latex_markup,config["pdf_filename"])


def get_config():
    config_file_name = parse_args()["config"]
    with open(config_file_name) as config_file:
        return json.load(config_file)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.json")
    return vars(parser.parse_args())


def populate_latex_src(config):
    with open("src/letter.tex") as letter_file:
        letter_content = letter_file.read()
    return (
        letter_content.replace(":name:", config["name"])
        .replace(":street:", config["street"])
        .replace(":zip:", config["zip"])
        .replace(":place:", config["place"])
        .replace(":subject:", config["subject"])
        .replace(":destinationaddress:", "destinationaddress")
        .replace(":opening:", config["opening"])
        .replace(":body:", config["body"])
        .replace(":closing:", config["closing"])
        .replace(":date:", config["date"])
    )


def compile_pdf(populated_latex_markup, pdf_filename):
    with open("tmp.tex", "w") as tmp_latex_file:
        tmp_latex_file.write(populated_latex_markup)
    os.system("pdflatex tmp.tex")
    os.system(f"mv tmp.pdf {pdf_filename}")


if __name__ == "__main__":
    main()
