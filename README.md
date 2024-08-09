<p align="center">
 <img width="100px" src="https://res.cloudinary.com/anuraghazra/image/upload/v1594908242/logo_ccswme.svg" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">GitHub Readme Stats</h2>
 <p align="center">Get dynamically generated GitHub stats on your READMEs!</p>
</p>
<div align="center">
    <a href="https://github.com/anuraghazra/github-readme-stats/actions">
      <img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg" />
    </a>
    <a href="https://github.com/anuraghazra/github-readme-stats/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/anuraghazra/github-readme-stats" />
    </a>
    <a href="https://codecov.io/gh/anuraghazra/github-readme-stats">
      <img alt="Tests Coverage" src="https://codecov.io/gh/anuraghazra/github-readme-stats/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/anuraghazra/github-readme-stats/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/anuraghazra/github-readme-stats?color=0088ff" />
    </a>
    <a href="https://github.com/anuraghazra/github-readme-stats/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/anuraghazra/github-readme-stats?color=0088ff" />
    </a>
    <a href="https://securityscorecards.dev/viewer/?uri=github.com/anuraghazra/github-readme-stats">
      <img alt="OpenSSF Scorecard" src="https://api.securityscorecards.dev/projects/github.com/anuraghazra/github-readme-stats/badge" />
    </a>
    <br />
    <br />
    <a href="https://vercel.com?utm\_source=github\_readme\_stats\_team\&utm\_campaign=oss">
    </a>
</div>
 <h1 align="center"><b>BUGS-MANAGEMENT</b></h1><hr>

## > GET THE FILES
```git
git clone https://github.com/Norx-Nishidh47/BUGS_MANAGEMENT.git
```
## > Install mysql connector 
```terminal
pip install mysql-connector-python
pip3 install mysql-connector-python
```
## > MYSQL Queries . 
### 1. Table Structure
```mysql
CREATE TABLE buginfo (
    bugID varchar(10) NOT NULL PRIMARY KEY,
    bugstatus int DEFAULT NULL,
    bugdesc text DEFAULT NULL,
    severity varchar(20) NOT NULL,
    reqdays int DEFAULT NULL,
    opendt timestamp DEFAULT CURRENT_TIMESTAMP,
    closedt timestamp DEFAULT CURRENT_TIMESTAMP,
    priority int DEFAULT NULL
);
```
```mysql
CREATE TABLE userinfo (
    username varchar(15) DEFAULT NULL,
    password varchar(30) DEFAULT NULL,
    email varchar(40) NOT NULL PRIMARY KEY,
    hash varchar(100) DEFAULT NULL
);
```
```mysql
CREATE TABLE assign (
    assign_to varchar(40) DEFAULT NULL,
    assigned_by varchar(40) DEFAULT NULL,
    bugID varchar(10) NOT NULL,
    FOREIGN KEY (bugID) REFERENCES buginfo(bugID)
);
```
### 2. Insert pre-def VALUES
```mysql
INSERT INTO buginfo (bugID, bugstatus, bugdesc, severity, reqdays, opendt, closedt, priority) VALUES
('APP-304', 3, 'Crash on startup', 'critical', 1, '2024-07-23 21:57:25', '2024-07-27 09:45:00', 1),
('DB-708', 2, 'Database connection timeout', 'database', 3, '2024-07-23 22:00:41', '2024-07-31 15:45:00', 3),
('MOB-102', 2, 'Search bar not showing properly', 'search hindrance', 2, '2024-07-23 21:49:31', '2024-07-25 20:03:19', 2),
('MOB-283', 1, 'Observe the differences in font styles, colors, and element alignment.', 'Medium', 5, '2024-07-22 17:50:09', '2024-07-27 00:00:00', NULL),
('NET-506', 1, 'Network latency issues', 'network', 2, '2024-07-23 22:00:41', '2024-07-29 08:20:00', 2),
('SEC-607', 3, 'Security vulnerability found', 'security', 5, '2024-07-23 22:00:41', '2024-07-30 13:00:00', 1),
('SYS-405', 2, 'Memory leak in module', 'performance', 4, '2024-07-23 22:00:41', '2024-07-28 11:30:00', 4),
('WEB-203', 1, 'Button alignment issue', 'UI bug', 3, '2024-07-23 21:56:39', '2024-07-26 14:15:00', 3);
```
```mysql
INSERT INTO userinfo (username, password, email, hash) VALUES
('Aayush Sapra', 'aayush@sapra', 'aayush@yt.com', 'U$«d&¢t@¿0+¦4_­'),
('Nishidh Singh', 'nishidh@13', 'ide@gmail.com', 'k!ªI#·D$¬h?°7#¿'),
('Nishidh', 'nishidh@123', 'nishidhsingh@gmail.com', 'p=´Z&ªa{³5;±v~¡'),
('Rihit Singh', 'Rihit@123', 'rihit34@outlook.com', 'P@²p&«p#¸q}¼Y@¿'),
('Tamanna Sharma', 'Nishidh@123', 'tamanna@outlook.com', 'X+¬p|¨Z¸G/¸w.®');
```
