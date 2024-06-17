# This Puppet manifest ensures the /var/www/html directory exists and is owned by the www-data user and group.
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Ensure Apache is installed and running
package { 'apache2':
  ensure => 'installed',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Package['apache2'],
}
