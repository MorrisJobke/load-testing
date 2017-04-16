


# Run Locust

Add following to your `/etc/hosts`:

```
1.2.3.4		locust1.local nextcloud-nfs.local netdata1.local
1.2.3.5		locust2.local nextcloud-os.local netdata2.local
```

```
ssh dcadmin@nextcloud-nfs.local
. /opt/locust-venv/bin/activate
cd /opt
locust --host=http://1.2.3.4
```
Open http://locust1.local 


```
ssh dcadmin@nextcloud-os.local
. /opt/locust-venv/bin/activate
cd /opt
locust --host=http://1.2.3.5
```

Open http://locust2.local

# Run blackfire profiling

```
ssh abc@1.2.3.4 # OR
ssh abc@1.2.3.5
blackfire curl -X PUT http://localhost/remote.php/dav/files/user0/test.dat -u user0:abc123abc\! --upload-file /tmp/sample-large.dat
```