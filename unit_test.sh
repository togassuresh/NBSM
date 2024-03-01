docker cp first_file.py flexsnap-agent:/tmp/first_file.py
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --list-disks --list-vm
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --list-disks --list-vms
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --list-disks --list-vms --list-snap
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --list-disks --list-vms --snap-lsit
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --list-disks --list-vms --snap-list
docker exec -it flexsnap-agent python /tmp/first_file.py --cloud azure  --use-credentials --list-disks --list-vms --snap-list
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --snap-list ---cloud azure  --use-credentials
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --snap-list --cloud azure  --use-credentials
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --snap-list --cloud aws  --use-credentials
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud aws  --use-credentials
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud gcp  --use-credentials
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud gcp  
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud aws  
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud aws  
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud azure
docker exec -it flexsnap-agent python /tmp/first_file.py  --list-disks --list-vms --list-snap --cloud azure --list-rg