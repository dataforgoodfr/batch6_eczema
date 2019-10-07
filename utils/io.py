import os

def raw(raw_data):
    print(raw_data)
    if raw_data == 'clinique' or 'full':
        clin = "Clinique-20190920T213539Z-001.zip"
        os.system(
            "wget https://datacorpus.s3-us-west-2.amazonaws.com/"
            "{} -P '../data/'".format(clin))
        os.system(f"unzip {clin}")
    if raw_data == 'transcriptom' or 'full':

        trans = "Transcriptome-20190920T214435Z-001.zip"
        os.system("wget https://datacorpus.s3-us-west-2.amazonaws.com"
                  f"/{trans} -P '../data/'")
        os.system(f"unzip {trans}")


def main():
    raw('clinique')
    print("oui")


if __name__ == '__main__':
    main()

