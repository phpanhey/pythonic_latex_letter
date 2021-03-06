# pythonic_latex_letter 👁💌🐍
pythonic latex letter creates a slick letter with signature. all you need to do is to adjust `config.json`.


## usage
the script depends on a `config.json` 

```json
{
    "name": "John Doe",
    "street": "John Doe Street 17",
    "zip": "29875",
    "place": "New Yrk",
    "subject": "Contract cancellation",
    "destinationaddress": [
        "Alphabet Inc.",
        "1600 Amphitheater",
        "Parkway Mountain View",
        "CA 94043 USA"
    ],
    "opening": "Hi there",
    "body": "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "closing": "Yours faithfully",
    "date": "08/27/2050",
    "pdf_filename": "john_doe_contract_cancellation.pdf"
}
```
typing
```bash
python3 pythonic_latex_letter.py
```
will generate a `john_doe_contract_cancellation.pdf`.
you can also specify your own config file by using the  `--config` option: 
```bash
python3 pythonic_latex_letter.py --config "cover_note_employer.json"
```

## dependecies
command line `pdflatex` is required.