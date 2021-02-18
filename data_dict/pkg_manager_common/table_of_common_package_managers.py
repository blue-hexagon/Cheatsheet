from markupsafe import Markup

table = Markup(
    """
    <table class="table table-sm style="white-space: nowrap;">
        <thead>
        <tr>
            <th>Intended Action</th>
            <th>RPM (Redhat, SUSE, Mandriva)</th>
            <th>Aptitude (Debian and derivatives)</th>
            <th>Pacman (Arch)</th>
            <th>Emerge (Gentoo)</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>Installing a package</td>
            <td><code>rpm -i </code><span class="text-muted small">&lt;package file&gt;</span></td>
            <td><code>aptitude install </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>pacman -S </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>emerge </code><span class="text-muted small">&lt;package&gt;</span></td>
        </tr>
        <tr>
            <td>Uninstalling a package</td>
            <td><code>rpm -e </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>aptitude remove </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>pacman -R </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>emerge --depclean </code><span class="text-muted small">&lt;package&gt;</span></td>
        </tr>
         <tr>
            <td>Searching for a package</td>
            <td><span class="text-muted small">N/A</span></td>
            <td><code>aptitude search </code><span class="text-muted small">&lt;string&gt;</span></td>
            <td><code>pacman -S -s </code><span class="text-muted small">&lt;string&gt;</span></td>
            <td><code>emerge -s </code><span class="text-muted small">&lt;string&gt;</span></td>
        </tr>
         <tr>
            <td>Listing installed packages</td>
            <td><code>rpm -qa</code></td>
            <td><code>dpkg -l -a</code></td>
            <td><code>pacman -Q -s '.*'</code></td>
            <td><code>equery list \*</code></td>
        </tr>

        <tr>
            <td>Listing files in package</td>
            <td><code>rpm -ql </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>dpkg -L </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>pacman -Q -l </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>equery files </code><span class="text-muted small">&lt;package&gt;</span></td>
        </tr>
                <tr>
            <td>Finding package containing file</td>
            <td><code>rpm -qf </code><span class="text-muted small">&lt;file&gt;</span></td>
            <td><code>dpkg -S </code><span class="text-muted small">&lt;file&gt;</span></td>
            <td><code>pacman -Q -o </code><span class="text-muted small">&lt;file&gt;</span></td>
            <td><code>equery belongs </code><span class="text-muted small">&lt;file&gt;</span></td>
        </tr>
        
        <tr>
            <td>Showing package description</td>
            <td><code>rpm -qi </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>aptitude show </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>pacman -S -i </code><span class="text-muted small">&lt;package&gt;</span></td>
            <td><code>emerge -s </code><span class="text-muted small">&lt;package&gt;</span></td>
        </tr>
       
       
        </tbody>
    </table>
    """
)
