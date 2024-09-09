from django.test import TestCase
from datetime import date

from .models import PursuitType, Pursuit, BlogPost, Link

class PursuitTypeModelTests(TestCase):
    def test_pursuittype_delete_fills_pursuit_default(self):
        """If a PursuitType is deleted, check all associated Pursuits set PursuitType to default"""
        default_pursuit_type = PursuitType.objects.get(pk=PursuitType.get_default_pk())
        pursuit_type = PursuitType(type="Passion")
        pursuit_1 = Pursuit(pursuit_type=pursuit_type,
                            internal_label="snowboarding",
                            img_path="snowboard_img_path",
                            title="I love snowboarding!",
                            description="This is a description about snowboarding")
        pursuit_2 = Pursuit(pursuit_type=pursuit_type,
                            internal_label="piano",
                            img_path="piano_img_path",
                            title="I play piano!",
                            description="This is a description about piano")
        pursuit_3 = Pursuit(pursuit_type=pursuit_type,
                            internal_label="swing_dancing",
                            img_path="swingdance_img_path",
                            title="I love to Swing Dance!",
                            description="This is a description about swing dancing")
        pursuits = [pursuit_1, pursuit_2, pursuit_3]

        pursuit_type.save()
        for pursuit in pursuits:
            pursuit.save()

        # Check Pursuit Types match with assigned Pursuit Type before deletion
        for pursuit in Pursuit.objects.all():
            self.assertEquals(pursuit_type, pursuit.pursuit_type)

        # Check Pursuit Types match with default Pursuit Type after deletion
        pursuit_type.delete()
        for pursuit in Pursuit.objects.all():
            self.assertEquals(default_pursuit_type, pursuit.pursuit_type)


    def test_pursuit_delete_fills_blogpost_default(self):
        """If a Pursuit is deleted, check all associated BlogPosts replace deleted Pursuit with default"""
        default_pursuit = Pursuit.objects.get(pk=Pursuit.get_default_pk())
        pursuit = Pursuit(internal_label="cs_profiles",
                          img_path="csprofiles_img_path",
                          title="CS Profiles : An Interesting title",
                          description="Description about CS Profiles")
        blog_post_1 = BlogPost(pursuit=pursuit,
                               title="CS Profiles : Design Decisions, Scope, Plan!",
                               date=date.today(),
                               preview="Preview about this blog post",
                               article="The entirety of the blog post")
        blog_post_2 = BlogPost(pursuit=pursuit,
                               title="CS Profiles : Dev Log 8",
                               date=date.today(),
                               preview="Preview about this blog post",
                               article="The entirety of the blog post")
        blog_post_3 = BlogPost(pursuit=pursuit,
                               title="CS Profiles : Dev Log 2",
                               date=date.today(),
                               preview="Preview about this blog post",
                               article="The entirety of the blog post")
        blog_posts = [blog_post_1, blog_post_2, blog_post_3]

        pursuit.save()
        for blog_post in blog_posts:
            blog_post.save()

        # Check setup is correct
        for blog_post in BlogPost.objects.all():
            self.assertEquals(pursuit, blog_post.pursuit)

        # After Pursuit deletion, check Blog Posts revert their Pursuit to default
        pursuit.delete()
        for blog_post in BlogPost.objects.all():
            self.assertEquals(default_pursuit, blog_post.pursuit)


    def test_pursuit_delete_cascadedeletes_links(self):
        """If Pursuit is deleted, check all associated Links are also deleted"""
        pursuit = Pursuit(internal_label="cs_profiles",
                          img_path="csprofiles_img_path",
                          title="CS Profiles : An Interesting title",
                          description="Description about CS Profiles")
        link_1 = Link(pursuit=pursuit,
                      text="Blog Series",
                      link="link to GitHub")
        link_2 = Link(pursuit=pursuit,
                      text="Website",
                      link="link to Website")
        link_3 = Link(pursuit=pursuit,
                      text="extras",
                      link="link to extra stuff")
        links = [link_1, link_2, link_3]
        pursuit.save()
        for link in links:
            link.save()

        # Check all links are there with correct pursuit associated
        for link in Link.objects.all():
            self.assertEquals(pursuit, link.pursuit)

        # Check all links are removed after pursuit is deleted
        pursuit.delete()
        self.assertEquals(len(list(Link.objects.all())), 0)
