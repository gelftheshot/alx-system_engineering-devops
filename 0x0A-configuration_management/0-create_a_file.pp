#this is the code to create file inside /temp with some permistions
file {'/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
