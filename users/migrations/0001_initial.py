# Generated by Django 4.1.1 on 2022-09-19 06:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="User Email"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Is Active"),
                ),
                (
                    "is_student",
                    models.BooleanField(default=False, verbose_name="Is Student"),
                ),
                (
                    "is_teacher",
                    models.BooleanField(default=False, verbose_name="Is Teacher"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="useraccount",
            index=models.Index(fields=["id"], name="users_usera_id_d06693_idx"),
        ),
        migrations.AddIndex(
            model_name="useraccount",
            index=models.Index(fields=["email"], name="users_usera_email_482885_idx"),
        ),
        migrations.AddIndex(
            model_name="useraccount",
            index=models.Index(
                fields=["is_active"], name="users_usera_is_acti_6fac38_idx"
            ),
        ),
    ]
