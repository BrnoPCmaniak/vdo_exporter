# vdo_exporter
VDO is a kernel subsystem that provides compression and deduplication to a Linux device. This project provides a Python2 based Prometheus exporter
 for VDO volume statistics. Once exported, you may visualize the data and define alerts within Prometheus itself, or
  define dashboards and alerts in systems like Grafana.  

## Background  
Writing an exporter for Prometheus would normally entail using the prometheus-client Python package, but at the time of writing
the rpm for this wasn't available for CentOS or RHEL. So this project just uses standard Python features to implement
the exporter (a Prometheus client is just a HTTP endpoint anyway!)

## Installation  
1. download and extract the archive  
2. cd to the vdo_exporter directory  
3. install vdo_exporter  
```bash
> python setup.py install --record installed_files
```
Optionally copy the systemd file
```bash
> cp systemd/vdo_exporter.service /etc/systemd/system
> systemctl daemon-reload
> systemctl enable vdo_exporter
> systemctl start vdo_exporter
```

## Running  
By default the vdo_exporter daemon will bind to 0.0.0.0, listening on port 9286. You'll see
the success of scrape requests in the daemon's output.  



## Prometheus Configuration  
Update prometheus.yml to include a scrape job for the hosts that have the vdo_exporter running.  
e.g. under scrape_configs
```yaml
  # VDO enabled hosts
  - job_name: "vdo_stats"
    static_configs:
      - targets: [ '10.90.90.82:9286', '10.90.90.123:9286', '10.90.90.121:9286']
```
then reload Prometheus (SIGHUP)  

*NB.   
if you're interested in bringing the VDO stats together with Ceph, you should use DNS names instead of IP addresses within the scrape definition. This will allow your promQL to 'match' across metrics based on "exported_instance" and "instance".*

## Grafana Configuration  
I've included a dashboard to show some of the stats the exporter provides. Just import the
the 'VDO_Information.json' dashboard from the grafana subdirectory into Grafana, then open the dashboard.  

You should see something like;  

![screenshot](/screenshots/vdo_information_demo.gif)
