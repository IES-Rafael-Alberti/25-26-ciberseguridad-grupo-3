# Informe técnico

# 1. Resumen Ejecutivo

## 1.1 Línea Temporal

# 2. Introducción

## Verificación de integridad

- Imagen del disco del PC de Lassandra

![img](img/hash-disco-img.png)

![img](img/hash-disco-zip.png)

- Extracción copia de seguridad ADB - Teléfono X25 de Atalus

![img](img/HASH_ATALUS_GRASSTEM_AB.png)

- Extracción copia de seguridad ADB - Teléfono Xiaomi Redmi Note 11 de Camillo

![img](img/HASH_CAMILO_RICHBALD_AB.png)

- Extracción copia de seguridad ADB - Teléfono Xiaomi Redmi Note 11 de Lassandra

![img](img/HASH_LASSANDRA_CORDAIS_AB.png)

- Imagen de la tarjeta SD de la Cámara IP Imou

![img](img/HASH_IMAGEN_SD_AD.png)

- Extracción conversaciones Telegram - Teléfono Xiaomi Redmi Note 11 de Lassandra (víctima)

![img](img/HASH_TELEGRAM_LASSANDRA.png)

- Extracción conversaciones WhatsApp - Teléfono Xiaomi Redmi Note 11 de Lassandra (víctima)

![img](img/HASH_WHATSAPP_LASSANDRA.png)

- Extracción conversaciones WhatsApp - Teléfono X25 de Atalus (principal sospechoso)

![img](img/HASH_WHATSAPP_ATALUS.png)

- Extracción conversaciones WhatsApp - Teléfono Xiaomi Redmi Note 11 de Camillo (cómplice)

![img](img/HASH_WHATSAPP_CAMILO.png)

- Extracción copia de seguridad del servidor Instagram de Lassandra (víctima)

![img](img/HASH_INSTAGRAM_LASSANDRA.png)

- Extracción copia de seguridad del servidor Google de Lassandra (víctima)

![img](img/GOOGLE_DATA_LASSANDRA.png)

- Extracción copia de seguridad del servidor Google de Atalus (principal sospechoso)

![img](img/GOOGLE_DATA_ATALAUS.png)

- Extracción copia de seguridad del servidor Google de Camillo (cómplice)

![img](img/GOOGLE_DATA_CAMILO.png)


## Verificación de Integridad de las Evidencias

| Adquisición | Tamaño (Bytes) | HASH SHA-256 | HASH MD5 | HASH SHA1 |
|---|---|---|---|---|
| adb-backup-Atalus-Grasstem.ab | 29.013.457 | e64e952c3f43c235baf5d83f8cea1a86d7640821baefcbe89c480b0fff7688cf | 69E1E89FD971E5817A2C8C6279A80601 | 7EA6F0F6CADE8F6FA55C01C51C683216CD53D463 |
| adb-backup-Camillo-Richbald.ab | 158.652 | 9c9c983de848c7b600a8f97a191b2fc7f9c77f5826de42fef93b410094bfac43 | 927713F263F80B4B747F65E58A1BDD53 | 985B4C25B4B72201A7ED591338FBDA9629E12154 |
| adb-backup-Lassandra-Cordalis.ab | 523.014 | 40e6f12cf248468c2849aa2c8094d186b0264bb758d4839ee190486721da013a | DDFF7DFE751359D2C7ED4E743B91A774 | FC560A40196DC92D463C172481FBAF166D223C76 |
| Disco-pc-infectado-ducky.img.zip | 5.773.164.742 | a61abd7be758d6f494e84fcb743e78e65d3b30f95ffab7e65839fceaf3f7b21d | F5C17537B21F0E048237B9B6B1865548 | 3A7847F7BF9FE91D2794ED3B12CAC9953FADD63C |
| disco-pc-infectado-ducky.img | 53.687.091.200 | 33a147e409a2400a762845932c9cde7ce280fc944f4a6e6e50d8e0aece2f2ef0 | 39A7E7302BEB29233E579B5AC5DC8D4E | 1BFB7525B55F84CF9ABF776DE273533DF84D2204 |
| Google-Data-Atalus-Grasstem.zip | 561.760 | e808a0bd5b9b55eb1ba536aa704c0e80164375e0fa96623f997ce5696a370a8a | 0013A261768BB2E03410A4EE6AFCDF1D | B5842A7BA3C0C5FE58CDE803987C22AF17E49C65 |
| Google-Data-Camillo-Richbald.zip | 408.222 | 47854017fc1f147d8426184519b1b21357f7876a9513ab40d093baf215ee6b3c | 7B06EAE50B2601998BDB3EFB0969854A | B0BD8808EB5A00DFD77F98E8E4EC259719A02B45 |
| Google-Data-Lassandra-Cordalis.zip | 588.782 | 0a1989aeae247aaba70621795127d0b8de6be5d84e1a592269d457432c3c4ffa | 97AC95C08C9A2D5F3CD6780DEA9D27DC | ED5F5E2B68BC3021047AC7B6A1FD4B92B23F81D4 |
| imagen-sd.ad1 | 6.847.296 | 1beec3df0227eb8d26fc5810411a350fb62761b469fc380074d8978a7a048469 | 6DD44CD661AFED3D93EB96BDE12211BD | 22343FCE02A07CFE840104DA093715259F6738D1 |
| Instagram-lassandracordalis-20230504.zip | 735.897 | 07d015c094f37433e5f33634154544fc8d020c98cec038d32cab09e9d7e048f2 | 79B280F3FDA049A6B01DAF29BE56CDD4 | 515A23EB81ECC3E176DC2FEEB2DB5A0265ABFC2C |
| Telegram-Data-Lassandra-Cordalis.zip | 30.820.559 | 0e02fce437a698421c947b87c642704109d3d839d1a64ac1b365de1662cd3056 | 3ADBD1827E451EFA13F0DBB2227E7BC2 | 19B07D30A39565EE6AF03A90AA5FF5B64239797D |
| WhatsApp-Database-Atalus-Grasstem.zip | 131.501 | a50e56d3e6789b346cce39a90f392b88327000b3524c9cde231c7819a9c8da1f | 4591F56EE8ECCD774F896D43474104CD | D2A083436193A161E53F1D1E031CE0500ACBC69F |
| WhatsApp-Database-Camillo-Richbald.zip | 185.621 | c701ae767b8800ab15b201522611c23c23a5655d6d98b348e3b045076f5b8cef | 3478B015C867DFBCEECFCC49BC09C76E | B9BABDD79B25642826ECF3854842EBCDF915F222 |
| WhatsApp-Database-Lassandra-Cordalis.zip | 167.088 | 83b83a02e748e322933bbe29d98bdf8c21af8fd5457185a9d5ee903f9079e3c5 | 1477180EFC30A310B09166274D509C77 | 934014579462B514AA5D4A897558B17A6E63DFD0 |