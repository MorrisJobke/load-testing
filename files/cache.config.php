<?php

$CONFIG = [
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'memcache.distributed' => '\\OC\\Memcache\\Redis',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => array(
    'host' => 'localhost',
    'port' => 6379,
    'timeout' => 0,
  ),
  'htaccess.RewriteBase' => '/',
];
