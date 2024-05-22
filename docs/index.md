<img src="img/SMI-GitHub-Logo.png" class="align-right" alt="image" align="right" />

# Software for Medical Imaging

SMI contains several open-source applications and libraries for managing medical images, specifically DICOM. Our software has been designed, built, and validated in UK Trusted Research Environments (Safe Havens).

!!! Note
    This documentation repo is under early development. More information can be found in the documentation for each repository.

## Site Contents

-   [PICTURES](pictures)
-   [Acronyms](acronyms)
-   [Publications](publications)

## Our Software

<!-- Auto-generated from ../scripts/generate_repos_table.py. Do not manually edit! -->

| Name | Description |
| ---- | ----------- |
| [SmiServices](https://github.com/SMI/SmiServices) | Scale-able loading, linking and anonymisation of DICOM images for healthcare research environments (e.g. Safe Havens) |
| [BadMedicine.Dicom](https://github.com/SMI/BadMedicine.Dicom) | CLI / Library for generating dicom files for use in testing applications.  Images generated have 'realistic' tag data (based on aggregated tag data in dicom images taken in Scotland). |
| [IsIdentifiable](https://github.com/SMI/IsIdentifiable) | A tool for detecting identifiable information in data sources (CSV, DICOM, Relational Database and MongoDB) |
| [DicomTypeTranslation](https://github.com/SMI/DicomTypeTranslation) | FoDicom/FAnsiSql powered library for converting dicom types into database/C# types at speed. |
| [RdmpDicom](https://github.com/SMI/RdmpDicom) | Plugin for RDMP that adds support for load, linking (with EHR data in relational databases) and extracting anonymous DICOM images for researchers. |
| [dicompixelanon](https://github.com/SMI/dicompixelanon) | DICOM Pixel Anonymisation |
| [DicomTemplateBuilder](https://github.com/SMI/DicomTemplateBuilder) | Windows application for building and testing DICOM templates |
| [ctp-anon-minimal](https://github.com/SMI/ctp-anon-minimal) | A minimal re-packaging of the RSNA MIRC Clinical Trials Processor (CTP), mainly providing the DICOMAnonymizer class |
| [CogStack-SemEHR](https://github.com/SMI/CogStack-SemEHR) | Semantic parsing of Electronic Health Records |
| [DicomLoadScript](https://github.com/SMI/DicomLoadScript) |  |
| [DqeToImagingJson](https://github.com/SMI/DqeToImagingJson) |  |
| [SCANDAN](https://github.com/SMI/SCANDAN) |  |
| [StructuredReports](https://github.com/SMI/StructuredReports) | DICOM Structured Reports |
| [ansible](https://github.com/SMI/ansible) | Automated deployment of the SMI software stack |
| [ctp-anon-cli](https://github.com/SMI/ctp-anon-cli) | A CLI tool to anonymise files using the RSNA MIRC Clinical Trials Processor (CTP) DICOM Anonymizer |
| [db_analysis](https://github.com/SMI/db_analysis) | Various scripts used to query any monitor MongoDB |
| [dicom-packager](https://github.com/SMI/dicom-packager) | Scripts to package-up directories of DICOM files for transfer |
| [dicom-to-minio](https://github.com/SMI/dicom-to-minio) | Script to upload directories of DICOM files to MinIO |
| [metacat](https://github.com/SMI/metacat) | Custom medical imaging metadata catalogue including classification based on DICOM metadata |
| [nlp2phenome](https://github.com/SMI/nlp2phenome) | Infer patient phenotypes from identified named entities (instances of biomedical concepts) |

## Contact

Please get in touch at <smi@epcc.ed.ac.uk> for all enquiries.
