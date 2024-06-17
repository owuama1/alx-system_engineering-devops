# This Puppet manifest increases the file descriptor limit for the holberton user

# Ensure the /etc/security/limits.d directory exists
file { '/etc/security/limits.d':
  ensure => 'directory',
}

# Create a configuration file to set the limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => 'present',
  content => 'holberton soft nofile 65536
holberton hard nofile 65536
',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

# Ensure PAM limits module is enabled in common-session
file_line { 'pam_limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session required pam_limits.so',
}
