file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => template('ssh_config.erb'),
}

# Make sure the private key file exists with the correct permissions
file { '/home/ubuntu/.ssh/school':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  # Optionally, you can manage the key content here or ensure it exists
  # content => 'YOUR_PRIVATE_KEY_CONTENT',
}
