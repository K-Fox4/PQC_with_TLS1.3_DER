# PQC-enabled DERMS Server and Client

Distributed Energy Resources Management System (DERMS) has two major purposes,
- Monitor the status of DER devices
- Control the active power supply of DER

This repository has code for both DERMS Server and Client, where DERMS Server is a web application
that monitors of all the DERs under its network and hosts REST APIs for gathering information from 
all its DERs, and DERMS Client that sends information to DERMS Server using REST APIs.

DERMS Server is a HTTPS server with TLS that is enabled with Post-Quantum Cryptography (PQC).
We have used Open Quantum Safe (OQS) [openssl](https://github.com/open-quantum-safe/openssl) for 
prototyping PQC into TLS 1.3 (IEEE 2030.5 standard).

### DERMS Server Environment
OS: Ubuntu 18.04    
Server: Nginx   
