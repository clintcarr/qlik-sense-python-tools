import shutil

numnodes = 4
maxconn = numnodes * 100

with open(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresql.conf', 'r') as postgresfile:
    with open(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresqlSP.conf', 'w+') as newpostgresfile:
        for line in postgresfile:
            if line.startswith('#listen_addresses'):
                newpostgresfile.write("listen_addresses = '*'")
            elif line.startswith("max_connections = 100"):
                newpostgresfile.write("max_connections = %d " % maxconn)
            else:
                newpostgresfile.write(line)

with open(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hba.conf', 'r') as hbafile:
    with open(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hbaSP.conf', 'w+') as newhbafile:
        for line in hbafile:
            if line.startswith('host    all             all             127.0.0.1/32            md5'):
                newhbafile.write('host    all             all             0.0.0.0/0            md5\n')
            else:
                newhbafile.write(line)

shutil.move(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresql.conf',
            'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresql_backup.conf')

shutil.move(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresqlSP.conf',
            'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\postgresql.conf')

shutil.move(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hba.conf',
            'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hba_backup.conf')

shutil.move(r'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hbaSP.conf',
            'C:\ProgramData\Qlik\Sense\Repository\PostgreSQL\9.3\pg_hba.conf')