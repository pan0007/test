require 'travis'
repos = Travis::Repository.find_all(owner_name: 'pan0007')
	.select{|repo| repo.slug == 'pan0007/test'} 
keys = ['COPR_LOGIN', 'COPR_TOKEN']
keys.each do |key|
	puts "Setting env var '#{key}' value #{ENV[key]}'"
end