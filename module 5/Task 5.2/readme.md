# 1 # etc/passwd
The / etc / passwd file contains a list of users known to the system. In the process of user registration, the system calls 
this file looking for the user ID and home directory. Each line of the file describes one user and   contains seven fields, separated by colons:
 * Home directory
 * Command interpreter.
 * Registration name
 * Encrypted password
 * User ID 
 * Personal data field.

# etc/group
The / etc / group file contains the names of the groups present in Linux and lists the members of each group, for example:
* daemon: x: 2: root, bi n, daemonIn this case, 

The system has a daemon group with an identifier equal to 2. This group includes users root, bin and daemon.Each entry in / etc / group represents one group and contains four fields:

    * Group name. By default, when a new user is created, his group is also created with the same name as the registration
    * Username.
    * An encrypted password or x to indicate the use of the / etc / gshadow file;
    * Group ID.
    * List of members separated by commas without spaces.
    
# NOBODY = NOLOGIN
 This user is intended to represent the user with the lowest permissions on the system. At best, this user and his group are not assigned to any file or directory (as owner). This user is in their respective group, which (according to the LSB) is also called "nobody" and in no other group
...
 * nano / etc / passwd
* gitdaemon: x: 124: 65534 :: / nonexistent: / usr / sbin / nologin
* postfix: x: 125: 131 :: / var / spool / postfix: / usr / sbin / nologin
* nvidia-persistenced: x: 122: 127: NVIDIA Persistence Daemon ,,,: / nonexistent: / usr / sbin / nologin

# 2 #UID

The UID is used to identify the user on the system and to determine which system resources the user can access. This is why the user ID must be unique.
* write command id user => uid=1000(user) gid=1000(user) groups=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare),129(vboxusers)
# 3 #GID

GID (Group ID)

# 4 #id -Gn name user , groups | wc -w

# 5 #To create a user, we use the command  useradd  "user " 

*-p = password
*-s = groups
## adduser is a simpler solution for creating users and in fact is an add-on over useradd, groupadd and usermod.

# 6 # usermod -l new_username old_username

# 7 #Skel_dir - user's skeleton directory. Contains standard files that define the standard user environment on the system. May be overridden by the administrator.

# 8 #8. How can I delete a user from the system (including his mailbox)?
Userdel - r $ username
Rm / var / mail / $ username 

# 9. What commands and keys should be used to lock and unlocking a user account?

Passwd –l $ username

Passwd –u $ username

/ etc / passwd - replace "x" with "*"

/ etc / shadow - put "!" at the beginning of the password
#10. How to remove a user's password and provide him with a password-free login

to change the password later?

Passwd –df $ username
# 11. Display the extended format of information about the catalog, talk about information columns displayed on the terminal.

# 12. What access rights exist and for whom (i.e., describe the main roles)? Briefly describe the acronym for access rights.

Rwx - read, write, execute (resp. 000..111, or 0..7)

777 - user, groups, others

# 13. What is the sequence in determining the relationship between the file and user?
 ## The relationship between the file and the user who started the process, the role is defined as:

    * If the UID of the file is the same as the UID of the process, the user is the owner of the file

    * If the GID of the file matches the GID of any group the user belongs to, he is a member of the group to which the file belongs.

    * If neither the UID nor the GID of the file overlaps with the process UID and the list of groups that the user running it is a member of, that user is an outsider.

     * It is in the role of the owner that the user (process) can change the shortcut of the file. The only thing that the owner cannot do with his file is to change the owner for him.
# 14. What commands are used to change the owner of a file (directory), and
also file access mode? Give examples, demonstrate onterminal.
* Chown [owner name] [path to file \ directory]
# 15. What is an example of octal representation of access rights?

Describe the umask command.

Umask - through a bitwise NOT, applies a mask \ prohibits setting the bit.

Umask 0 - everything can be changed

Umask 777 - prohibited

# 16. Give definitions of sticky bits and mechanism of identifier substitution.

Give an example of files and directories with these attributes.

Sticky bit - an extra bit used for directories (mostly) protecting files. The user cannot delete files that do not belong to meu.

Example folder / tmp
# 17. * What file attributes must be present in the command script?
 * chmod ugo +x
