# JumpRanking Sender ✉️

Tool to send data to JumpRanking Service

<br>

## ⚙️ Setup
<hr>

Generate new user and password according to your user and password for JumpRanking  Service.
Open [config.json](https://github.com/RDCH106/JumpRanking/tree/master/sender/config) file and replace user and password values. Password value is a digested value using the following command:

```bash
python -c "from hashlib import sha256; print(sha256('your_password'.encode('utf-8')).hexdigest())"
```
⚠️ Returned value must be introduced for password value. 🚫 **Not raw value!**
